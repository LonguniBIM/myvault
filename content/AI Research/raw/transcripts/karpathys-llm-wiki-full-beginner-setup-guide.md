---
type: source
title: "Karpathy'S Llm Wiki Full Beginner Setup Guide"
tags: [transcript, media]
related: []
created: 2026-04-30
updated: 2026-04-30
media_file: "Karpathy's LLM Wiki - Full Beginner Setup Guide-iXd0t60YmMw.m4a"
---

# Karpathy'S Llm Wiki Full Beginner Setup Guide

**Source**: `raw\video\Karpathy's LLM Wiki - Full Beginner Setup Guide-iXd0t60YmMw.m4a`
**Transcribed**: 2026-04-30

---

## Transcript

[00:00-00:03] There's a problem with the way most of us use AI right now.
[00:03-00:06] And once you see it, you're not going to be able to unsee it.
[00:06-00:09] When you upload documents to something like ChatGPT or Notebook
[00:09-00:13] LM and ask a question, the AI searches through your files,
[00:13-00:16] pulls out some relevant pieces, and gives you an answer.
[00:16-00:16] That works.
[00:16-00:18] But here's the thing.
[00:18-00:20] Ask a similar question tomorrow.
[00:20-00:23] And the AI does all of that work again from scratch.
[00:23-00:24] Nothing was saved.
[00:24-00:25] Nothing was built up.
[00:25-00:27] Every single question starts from zero.
[00:27-00:30] Andre Karpathi, one of the biggest names in AI,
[00:30-00:33] co-founder of OpenAI, former AI director at Tesla,
[00:33-00:36] recently shared an idea that fixes this problem.
[00:36-00:38] He calls it the LLM Wiki.
[00:38-00:41] And honestly, once you understand what it does,
[00:41-00:42] the old way of working with documents
[00:42-00:44] starts to feel broken.
[00:44-00:46] In this video, I'm going to walk you through exactly
[00:46-00:49] what the LLM Wiki is, why it matters.
[00:49-00:51] And then we're going to build one together from scratch.
[00:51-00:54] Step by step, you don't need to be technical.
[00:54-01:00] If you can create a folder on your computer, you can do this.
[01:00-01:03] Hi, I'm Jamie, and welcome to Teacher's Tech.
[01:03-01:05] So let me explain the problem a bit more clearly,
[01:05-01:07] because this is important.
[01:07-01:10] The way most AI tools handle your documents right now
[01:10-01:13] is called RAG, Retrieval Augmented Generation.
[01:13-01:14] You upload some files.
[01:14-01:15] You ask a question.
[01:15-01:18] The AI searches through those files,
[01:18-01:21] grabs the chunks that seem relevant and generates an answer.
[01:21-01:23] And that's fine for simple questions.
[01:23-01:25] But what if your questions require connecting ideas
[01:25-01:28] across five different documents?
[01:28-01:30] The AI has to find all those pieces
[01:30-01:33] and stitch them together every single time.
[01:33-01:34] There's no memory.
[01:34-01:35] There's no accumulation.
[01:35-01:37] Nothing compounds.
[01:37-01:38] Think about it like this.
[01:38-01:40] Imagine your researcher and you've
[01:40-01:42] been reading papers on a topic for weeks.
[01:42-01:45] With RAG, every time you ask the AI question,
[01:45-01:48] it's like it's never read any of those papers before.
[01:48-01:50] It starts fresh every time.
[01:50-01:51] That's the bottleneck.
[01:51-01:53] Karpathi's idea flips this completely.
[01:53-01:57] Instead of searching raw documents every time you ask a question,
[01:57-01:59] you have the AI read your documents once
[01:59-02:02] and build a structured wiki out of them.
[02:02-02:03] A real persistent knowledge base
[02:03-02:06] made of interlinked Markdown files.
[02:06-02:09] So when you add a new source, say a PDF or an article,
[02:09-02:11] the AI doesn't just store it for later.
[02:11-02:14] It actually reads it, extracts the key ideas,
[02:14-02:16] and integrates them into the wiki.
[02:16-02:18] It updates existing pages.
[02:18-02:20] It creates new pages for new concepts.
[02:20-02:22] It links related ideas together.
[02:22-02:24] And if the new source contradicts something already
[02:24-02:27] in the wiki, it flags that too.
[02:27-02:29] So over time, the wiki keeps growing
[02:29-02:32] and getting richer, the connections are already there.
[02:32-02:33] The synthesis is already done.
[02:33-02:37] When you ask a question, the AI is not starting from scratch.
[02:37-02:39] It's actually working from a pre-built, organized knowledge
[02:39-02:40] base.
[02:40-02:42] Here's how Karpathi describes it.
[02:42-02:46] He says, think of Obsidian as the IDE, the LLM
[02:46-02:49] as the programmer, and the wiki as the code base.
[02:49-02:51] You rarely write the wiki yourself.
[02:51-02:54] The AI does the writing and organizing.
[02:54-02:57] You focus on what goes in and what questions to ask.
[02:57-02:59] Now, the whole system has three layers,
[02:59-03:01] and they're very simple.
[03:01-03:03] Layer one, your raw sources.
[03:03-03:07] These are your original documents, like PDFs, articles,
[03:07-03:09] meeting nodes, whatever you're working with.
[03:09-03:12] The important thing is that these are read only.
[03:12-03:14] The AI reads them, but never changes them.
[03:14-03:16] This is your source of truth.
[03:16-03:18] Layer two is the wiki itself.
[03:18-03:20] This is a folder of markdown files
[03:20-03:22] that the AI creates and maintains.
[03:22-03:25] It's going to have things like an index page, concept pages,
[03:25-03:29] entity pages, summary comparisons, all entered linked,
[03:29-03:31] all maintained by the AI.
[03:31-03:33] Layer three, the schema.
[03:33-03:35] This is basically a rules document.
[03:35-03:38] It tells the AI how to structure the wiki, how to handle
[03:38-03:41] new sources, how to format everything.
[03:41-03:44] If you're using Cloud Code, this would be your Cloud.MD file.
[03:44-03:47] If you'd follow my other Cloud Code series,
[03:47-03:48] you already know what that is.
[03:48-03:51] If you're new to Cloud Code, I'll put the link to my beginners
[03:51-03:52] video right up there.
[03:52-03:54] All right, let's get into the setup.
[03:54-03:55] Here's what we're going to need.
[03:55-03:56] First, Obsidian.
[03:56-03:58] This is a free note-taking app that
[03:58-04:00] works with plain markdown files.
[04:00-04:01] It's going to be our viewer.
[04:01-04:04] You can download it at obsidian.md. I'll put the link
[04:04-04:06] double-o in the description.
[04:06-04:08] And don't worry if you've never used Obsidian
[04:08-04:11] before, I'll walk you through the parts that matter.
[04:11-04:12] Second, an AI coding agent.
[04:12-04:14] I'm going to be using Cloud Code for this
[04:14-04:17] because this is what I've been using in my series,
[04:17-04:19] and it works really well for this.
[04:19-04:22] But you could also use opening a codex, cursor,
[04:22-04:25] or other tools that can read and write files on your computer.
[04:25-04:27] Now, I just want to point out I'm using Obsidian
[04:27-04:30] because it has the graph view that makes the connections
[04:30-04:31] really visual.
[04:31-04:33] But this is just a folder of markdown files.
[04:33-04:36] You could use VS Code or any text editor,
[04:36-04:38] whatever you're most comfortable with.
[04:38-04:39] Once you've got Obsidian installed,
[04:39-04:41] just go ahead and open it.
[04:41-04:42] And the first thing what I'm going to do
[04:42-04:46] is just go and create a new vault you'll see right here.
[04:46-04:48] And this is just a fancy name for folder.
[04:48-04:50] So I'm going to go create.
[04:50-04:53] And I'm going to call this one LLM Weiki.
[04:53-04:55] And I'm just going to save it somewhere simple.
[04:55-04:58] I'm just going to put it into my documents here.
[04:58-04:59] You'll see there.
[04:59-05:00] And you can put it where you'd like.
[05:00-05:02] I'm going to go and hit create.
[05:02-05:04] Now we need to set up a folder structure.
[05:04-05:06] I'm going to create three folders.
[05:06-05:08] The first one's going to be raw.
[05:08-05:10] I'm just clicking right up here, new folder,
[05:10-05:12] and I'm going to call it raw.
[05:12-05:14] The AI will read from this, but never
[05:14-05:16] change anything in here.
[05:16-05:19] The second folder is going to be Weiki.
[05:19-05:24] This is where the AI will build and maintain all of its pages.
[05:24-05:27] And the third folder is going to be called templates.
[05:27-05:29] This template's folder is optional.
[05:29-05:31] If you wanted to manually create notes
[05:31-05:33] in Obsidian with the consistent format,
[05:33-05:35] you could put a template right in here.
[05:35-05:37] But since Claude is going to be creating all
[05:37-05:40] of our Weiki pages for us, we don't need it for this tutorial.
[05:40-05:43] It's just here as a point to tell you about.
[05:43-05:45] So here's what our structure looks like.
[05:45-05:48] We have our Weiki, templates, and raw.
[05:48-05:50] Nothing too complicated with this.
[05:50-05:51] Now, here's the important part.
[05:51-05:53] We need to create the schema file.
[05:53-05:57] The rules document that tells the AI how to operate the Weiki.
[05:57-05:58] If you're using Claude code, you're
[05:58-06:03] going to create a file called Claude.md in the root of your fault.
[06:03-06:06] So this is the file that Claude code reads automatically
[06:06-06:07] when it opens a project.
[06:07-06:09] So I'm going to give you a starter template
[06:09-06:10] that you can copy.
[06:10-06:12] It's linked down below in the description.
[06:12-06:14] But let me walk you through what's in it.
[06:14-06:17] Now, first of all, I'm just going to bring the Claude.md
[06:17-06:19] file into the root right here.
[06:19-06:21] So I'm just going to drop it so we can have it here.
[06:21-06:23] You can see my other folders are here.
[06:23-06:26] But here's the Claude.md file.
[06:26-06:29] So if I click on it, you're going to be able to see what's in it.
[06:29-06:31] Now, first, the purpose rate here.
[06:31-06:33] So this is the purpose of the Weiki.
[06:33-06:35] What's the knowledge base about?
[06:35-06:38] So in our template, I've set this to planning a trip to Japan
[06:38-06:41] because this is what we're going to do in the demo today.
[06:41-06:44] But when you download this file,
[06:44-06:47] this is the one line you can change to match whatever
[06:47-06:49] you're going to be building a Weiki about.
[06:49-06:52] If you're researching renewable energy, change it to that.
[06:52-06:55] If you're wanting to track books that you want to learn
[06:55-06:56] from, change it to that.
[06:56-06:58] Everything else in the template works as is.
[06:58-07:01] The purpose of the line is the only thing
[07:01-07:03] that you really need to customize to get started.
[07:03-07:05] Second, the folder structure.
[07:05-07:07] Where are the raw resources?
[07:07-07:09] Where's the Weiki output?
[07:09-07:10] What goes where?
[07:10-07:12] Third, the ingest workflow.
[07:12-07:16] When you add a new source document, what should the AI do?
[07:16-07:19] The basic steps are read the document, extract key concepts,
[07:19-07:22] create the update Weiki pages, update the index,
[07:22-07:24] and log what changed.
[07:24-07:26] Fourth, page formatting rules.
[07:26-07:28] Things like every page should have a summary at the top.
[07:28-07:31] Every claim should reference its source.
[07:31-07:34] Pages should link to related concepts.
[07:34-07:37] And fifth, the question answering behavior.
[07:37-07:40] When you ask the AI a question, it should consult
[07:40-07:43] the Weiki first, cite its sources,
[07:43-07:46] and tell you when something is uncertain.
[07:46-07:47] Now, don't overthink this.
[07:47-07:49] The template I'm giving you gives you
[07:49-07:50] a solid starting point.
[07:50-07:53] You can always refine it as you go.
[07:53-07:54] That's actually part of the process.
[07:54-07:57] The schema evolves as the Weiki grows.
[07:57-08:00] I'm also going to add this obsidian extension here.
[08:00-08:01] It's a web clipper, so I'm going to go ahead
[08:01-08:03] and add this to Chrome.
[08:03-08:05] It's free to do, and what it's going to do
[08:05-08:08] is convert any web articles into a markdown file,
[08:08-08:09] so it's super handy.
[08:09-08:11] All right, now here comes the fun part.
[08:11-08:14] Let us feed the Weiki with its first document.
[08:14-08:17] Now, I'm going to drop an article into the raw folder.
[08:17-08:18] And for this demo, I'm going to be planning
[08:18-08:19] a trip to Japan.
[08:19-08:21] So I'm going to start with a travel blog post
[08:21-08:23] about visiting Tokyo.
[08:23-08:25] Things to do, like neighborhoods, to explore,
[08:25-08:26] that kind of thing.
[08:26-08:28] I'm going to save this as a markdown
[08:28-08:31] with the extension that we just installed.
[08:31-08:35] So if I go up top, you can see I have the extension here.
[08:35-08:39] And I could go directly to obsidian, or I can download it.
[08:39-08:41] So I am going to just, or I could copy paste it over to.
[08:41-08:44] I'm going to hit save as, now I'm going to hop back over
[08:44-08:46] to obsidian here.
[08:46-08:49] So that's just in my downloads folder right now.
[08:49-08:51] So I can see it.
[08:51-08:52] I can drag it over.
[08:52-08:54] And where do I want it?
[08:54-08:56] I want to put it in my raw.
[08:56-08:58] So if I click, here it is now.
[08:58-09:01] Here's that article, all that information
[09:01-09:03] right in here into my raw folder.
[09:03-09:06] And by the way, your sources don't have to be markdown files.
[09:06-09:10] If you have PDFs, just drag them straight into the raw folder.
[09:10-09:12] Cloud code can read PDFs natively,
[09:12-09:14] same with text files, same with markdown.
[09:14-09:16] Whatever your format documents are in,
[09:16-09:19] just drop them in and cloud will handle it.
[09:19-09:21] Now I want to go in open cloud.
[09:21-09:22] But before I do that, I need to make sure
[09:22-09:25] that I'm pointing towards where we have this all set up.
[09:25-09:28] So I'm going to just change my directory
[09:28-09:30] to this right through here.
[09:30-09:32] You can see I put it in my documents.
[09:32-09:34] And this is what it's called.
[09:34-09:36] So we have our directory change.
[09:36-09:41] And now I'm going to go ahead and open up cloud.
[09:41-09:45] OK, so now I'm going to tell it to ingest the new source.
[09:45-09:48] So I'm just going to say, I just added a new source to the raw folder.
[09:48-09:51] Please read it and update the week.
[09:51-09:52] And watch what's happening.
[09:52-09:55] Cloud is reading the article.
[09:55-09:57] It's creating the weeky pages.
[09:57-09:59] And there's the summary of the article.
[09:59-10:03] Here's the pages for different neighborhoods, like all through here.
[10:03-10:06] You can see all the different weeky pages here
[10:06-10:07] that is planning to create.
[10:07-10:10] And if this looks good, I'm going to tell it to go ahead.
[10:10-10:12] But you can see how I can adjust the scope as well.
[10:12-10:14] I'm just going to say go ahead.
[10:14-10:17] OK, you can see after about three minutes it's all done.
[10:17-10:21] But let's go check out Obsidian and what's happening over there.
[10:21-10:23] All right, let's open up the weeky.
[10:23-10:26] So you look at this, we have structured pages.
[10:26-10:31] If we click on any of these here, we have links to all of these.
[10:31-10:33] And if I go over to graph view,
[10:33-10:35] take a look at this.
[10:35-10:37] You can see the connections forming.
[10:37-10:39] This is one document.
[10:39-10:42] Imagine what this looks like after 20 sources.
[10:42-10:44] Now, this is where it gets really interesting.
[10:44-10:46] Let me add a second source.
[10:46-10:48] We're going to do this food guide here to Japan.
[10:48-10:50] I'm going to do what I did last time.
[10:50-10:53] I'm just going to go ahead and make sure that I save it.
[10:53-10:54] And I'll bring it back over Obsidian.
[10:54-10:59] Then I'll tell Claw to ingest it.
[10:59-11:00] Let's say the exact same thing.
[11:00-11:02] I just added new sources to the raw folder.
[11:02-11:05] Please read it and update the weeky.
[11:05-11:06] Now, look at this.
[11:06-11:09] So Claw isn't just creating new pages.
[11:09-11:12] It's actually updating the neighborhood pages
[11:12-11:13] as well that it already made.
[11:13-11:15] And you can kind of look specifically
[11:15-11:17] at the details how they're making those adjustments
[11:17-11:18] to each of these.
[11:18-11:20] This is the weeky doing its job.
[11:20-11:21] Now, look at the graph view.
[11:21-11:24] Now, more nodes, more connections.
[11:24-11:27] The weeky is getting smarter with every source we add.
[11:27-11:30] Now, let me ask a question that requires information
[11:30-11:31] from both sources.
[11:31-11:33] What neighborhood should I stay at
[11:33-11:35] if I want to be close to the best food
[11:35-11:38] and still near the major temples?
[11:38-11:39] And look at the answer.
[11:39-11:42] Claw is not searching the raw articles.
[11:42-11:44] It's pulling from the week, from the neighborhood pages,
[11:44-11:46] the food pages, the temple page.
[11:46-11:48] It's connecting dots that were spread across
[11:48-11:50] completely different sources.
[11:50-11:52] It's citing specific weeky pages.
[11:52-11:55] This is completely different from what you get
[11:55-11:56] with basic rag setup.
[11:56-11:59] One more thing I want to show you that I think is really clever.
[11:59-12:02] Karpathy talks about this idea of linting your weeky.
[12:02-12:06] Just like how a code linter checks your code for problems.
[12:06-12:09] You can periodically ask the AI to edit the whole weeky.
[12:09-12:12] It'll look for things like contradiction between pages,
[12:12-12:14] claims that might be outdated.
[12:14-12:17] Pages that have no links pointing to them
[12:17-12:19] or like orphan pages and concepts that are mentioned
[12:19-12:22] but don't have any of their own page yet.
[12:22-12:24] We can just say something like this.
[12:24-12:26] Please lint the weeky.
[12:26-12:28] Now, Claw is going to go through everything
[12:28-12:30] and give you a report.
[12:30-12:33] This is how you keep your weeky healthy as it grows.
[12:34-12:37] And look what it gives me back here.
[12:37-12:40] The different checks from orphan pages to broken links.
[12:40-12:42] This is telling me that it's structurally sound
[12:42-12:43] which I expected since we only have
[12:43-12:45] two different articles in this.
[12:45-12:47] And it points out the biggest gap here
[12:47-12:49] is the uningested food source.
[12:49-12:52] And even makes the offer to fix the citation issues.
[12:52-12:54] So what would you actually use this for?
[12:54-12:55] Here are some ideas.
[12:55-12:57] If you're a student or a researcher,
[12:57-13:00] build a weeky as you read papers and articles
[13:00-13:01] on a topic.
[13:01-13:03] By the end, you have this structured knowledge base,
[13:03-13:05] just not a pile of highlighted PDFs.
[13:05-13:08] If you're a teacher, feed in curriculum documents,
[13:08-13:11] professional development materials and articles,
[13:11-13:14] build a personal teaching weeky that grows over time.
[13:14-13:16] If you're a business, feed in meeting notes,
[13:16-13:19] customer call transcripts and project documents.
[13:19-13:23] So this allows new team members to browse this organized weeky
[13:23-13:25] instead of digging through Slack history.
[13:25-13:28] If you're just a curious person who reads a lot,
[13:28-13:30] you use it to track what you learn from books,
[13:30-13:32] podcasts and articles.
[13:32-13:34] It's like building your own personal encyclopedia.
[13:34-13:37] The pattern works anywhere you're accumulating knowledge
[13:37-13:39] over time and you want it organized
[13:39-13:41] rather than just scattered.
[13:41-13:43] Okay, let me be straight about the limitations
[13:43-13:44] because this isn't magic.
[13:44-13:47] First, this works best at personal scale.
[13:47-13:49] Karpathy talks about having weekies
[13:49-13:51] of around a hundred articles.
[13:51-13:52] If you're trying to build something
[13:52-13:54] with tens of thousands of pages,
[13:54-13:56] you're gonna want more infrastructure
[13:56-13:58] than just some markdown files.
[13:58-14:00] Second, garbage in, garbage out.
[14:00-14:03] The weeky is only as good as the sources you feed it.
[14:03-14:05] You still need to curate what goes in.
[14:05-14:08] Third, you do need a coding agent to make this work.
[14:08-14:10] Obsidian by itself doesn't do any of this.
[14:10-14:13] The AI is the engine, so you need to access
[14:13-14:16] something like Cloud Code, CodeX or a similar tool.
[14:16-14:18] And fourth, the AI can make mistakes.
[14:18-14:22] It might miscategorize something or a misconnection.
[14:22-14:23] That's why the Lint feature exists.
[14:23-14:25] If you want to review what it builds,
[14:25-14:27] especially earlier on.
[14:27-14:28] But with all that said,
[14:28-14:31] this is generally one of the most practical AI workflows
[14:31-14:32] I've seen.
[14:32-14:33] It solves real problems.
[14:33-14:36] It's free to set up and your data stays
[14:36-14:40] on your computer in plain text files that you own.
[14:40-14:42] And that's the LLM weeky, a personal knowledge base
[14:42-14:44] that the AI builds and maintains for you
[14:44-14:46] that actually gets better over time
[14:46-14:49] instead of starting from scratch on every question.
[14:49-14:52] I'll have the schema template and all the links you need
[14:52-14:54] in the description below.
[14:54-14:57] If you want to learn Cloud Code so you can use it for yourself,
[14:57-14:59] my beginners guide is down there also.
[14:59-15:01] Thanks for watching this time on Teacher's Tech.
[15:01-15:04] I'll see you next week with more tech tips and tutorials.
