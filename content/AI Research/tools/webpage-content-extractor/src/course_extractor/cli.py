"""Typer CLI: inspect / extract / validate."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer

from .config import Config
from .util import logging as log

app = typer.Typer(add_completion=False, help="Webpage-Complete lesson content extractor")


def _parse_formats(value: str) -> list[str]:
    return [v.strip().lower() for v in value.split(",") if v.strip()]


@app.command()
def inspect(
    input: Path = typer.Option(..., "--input", "-i", help="ZIP / HTML / directory"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """Print discovered lesson structure without writing any output."""
    log.set_verbose(verbose)
    from .pipeline import parse_document

    config = Config(verbose=verbose)
    config.resolve_tools()
    doc, html_path, root_dir, _ = parse_document(input, config)
    images = list(doc.iter_images())
    audios = list(doc.iter_audio())
    typer.echo(f"Title: {doc.source.title}")
    typer.echo(f"Adapter: {doc.source.adapter}")
    typer.echo(f"Blocks: {len(doc.blocks)}")
    typer.echo(f"Images: {len(images)}")
    typer.echo(f"Audio references: {len(audios)}")
    for a in audios:
        typer.echo(f"  - audio #{a.placeholder_index}: {a.duration_label} "
                   f"({a.duration_seconds}s)")
    if doc.warnings:
        typer.echo(f"Warnings: {len(doc.warnings)}")


@app.command()
def extract(
    input: Path = typer.Option(..., "--input", "-i", help="ZIP / HTML / directory"),
    output: Path = typer.Option(Path("./output"), "--output", "-o"),
    formats: str = typer.Option("md,docx,json", "--formats", "-f"),
    mode: str = typer.Option("exact", "--mode", help="exact | clean"),
    transcribe: bool = typer.Option(True, "--transcribe/--no-transcribe"),
    whisper_model: str = typer.Option("small", "--whisper-model"),
    language: Optional[str] = typer.Option("en", "--language"),
    tolerance: float = typer.Option(1.0, "--duration-tolerance"),
    soffice: Optional[str] = typer.Option(None, "--soffice"),
    ffprobe: Optional[str] = typer.Option(None, "--ffprobe"),
    render_docx: bool = typer.Option(False, "--render-docx", help="QA-render DOCX to PDF"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """Extract a lesson to Markdown / DOCX / manifest with audio transcripts."""
    log.set_verbose(verbose)
    from .pipeline import run_extract
    from .qa.validator import validate_output_dir

    config = Config(
        mode=mode,
        formats=_parse_formats(formats),
        transcribe=transcribe,
        whisper_model=whisper_model,
        whisper_language=language,
        duration_tolerance=tolerance,
        soffice_path=soffice,
        ffprobe_path=ffprobe,
        render_docx=render_docx,
        verbose=verbose,
    )
    result = run_extract(input, output, config)
    typer.echo("")
    typer.echo(f"Output: {result.output_dir}")
    for name, path in result.outputs.items():
        typer.echo(f"  {name}: {path.name}")

    problems = validate_output_dir(result.output_dir)
    if problems:
        typer.echo("")
        typer.echo("Validation problems:")
        for p in problems:
            typer.echo(f"  ! {p}")

    if render_docx and "docx" in config.formats:
        _render_docx_qa(result.output_dir, config)


@app.command()
def validate(
    output_dir: Path = typer.Option(..., "--output-dir", "-d", help="An extracted lesson folder"),
) -> None:
    """Validate a previously extracted output folder."""
    from .qa.validator import validate_output_dir

    problems = validate_output_dir(output_dir)
    if not problems:
        typer.echo("OK: no structural problems found.")
        raise typer.Exit(0)
    for p in problems:
        typer.echo(f"! {p}")
    raise typer.Exit(1)


def _render_docx_qa(out_dir: Path, config: Config) -> None:
    import subprocess

    docx = next(out_dir.glob("*.docx"), None)
    if not docx or not config.soffice_path:
        log.warn("skip DOCX QA render (soffice not found or no docx)")
        return
    qa_dir = out_dir / "qa"
    qa_dir.mkdir(exist_ok=True)
    try:
        subprocess.run(
            [config.soffice_path, "--headless", "--convert-to", "pdf",
             "--outdir", str(qa_dir), str(docx)],
            check=True, capture_output=True, timeout=180,
        )
        pdf = next(qa_dir.glob("*.pdf"), None)
        if pdf and pdf.stat().st_size > 0:
            log.info("DOCX QA render OK: {}", pdf)
        else:
            log.warn("DOCX QA render produced no PDF")
    except Exception as exc:  # noqa: BLE001
        log.warn("DOCX QA render failed: {}", exc)


if __name__ == "__main__":
    app()
