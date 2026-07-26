---
type: entity
title: "7-Hour Chart"
tags: [killzone, session, day-trading]
related: [daily-profiles, expansion-model-am, the-market-lens-2025-expansion-model]
created: 2026-05-07
updated: 2026-05-07
---

# 7-Hour Chart

**Type**: Timeframe / analytical tool

**Used in**: Expansion Model (AM / The Market Lens)

---

## Description

Timeframe 7 giờ chia daily candle thành 3 candles bằng nhau, tương ứng với 3 market sessions chính. Đây là công cụ để simplify daily profiling trong Expansion Model.

## Three 7H Candles

| Candle | Time (UTC-5) | Session | Reversal % | Range % | Same-dir Close % |
|--------|-------------|---------|-----------|---------|-----------------|
| **18:00 candle** | 18:00–01:00 | Asia | 40% | 17% | 58% |
| **01:00 candle** | 01:00–08:00 | London | 21% | 24% | 62% |
| **08:00 candle** | 08:00–15:00 | New York | 39% | 59% | 83% |

*Data từ expansion days only (ngày đóng cửa là expansion)*

## Trading Logic per Candle

- **18:00**: Không trade. Chỉ đọc context sau khi close
- **01:00**: Entry khả dụng nếu 18:00 cung cấp opposing swing. Timeframe: 30m/15m
- **08:00**: Primary entry window. Đa số daily range xảy ra tại đây. Timeframe: 15m/5m

## Key Insight

08:00 candle vượt trội: 59% range, 83% close cùng hướng daily, 39% reversal probability → luôn ưu tiên be positioned or enter within 08:00 candle.

## Related Pages

- [[daily-profiles]] — Cách sử dụng 7H trong profiling
- [[expansion-model-am]] — Methodology context
