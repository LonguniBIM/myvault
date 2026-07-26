---
type: concept
title: "Daily Profiles (7H)"
tags: [killzone, session, execution, day-trading, high]
related: [7-hour-chart, expansion-model-am, change-in-state-of-delivery, expansion-rule, the-market-lens-2025-expansion-model]
created: 2026-05-07
updated: 2026-05-07
---

# Daily Profiles (7H)

**Definition**: Hệ thống xác nhận intraday bằng cách profiling 3 candles 7-giờ trong một ngày trading. Profile xác định khi nào bias đã được confirmed và entry hợp lệ.

**Source**: [[the-market-lens-2025-expansion-model]] — Section 5: Intraday Confirmation

---

## 4 Rules áp dụng cho mọi profile

1. **Không trade trong 18:00 candle** — dùng để quan sát, tạo context
2. **Previous 7H candle reversal confirmation** — nếu candle trước chưa establish intraday reversal → chờ candle tiếp theo
3. **Added confirmation trên 18:00 reversals** — nếu 18:00 tạo opposing swing, không trade 01:00 candle nếu swing còn nguyên; chỉ entry sau 08:00 mở
4. **Small wicks trên expansion days** — bullish expansion mở gần low-of-day; bearish mở gần high-of-day; không deviate xa daily open theo chiều ngược

---

## Ba Daily Profiles

### Profile 1: 18:00 Reversal

**Điều kiện**: 18:00 candle tạo opposing swing so với bias

| Step | Action |
|------|--------|
| 1 | 18:00 candle forms opposing swing (low nếu bullish bias; high nếu bearish) |
| 2 | Không trade 01:00 candle nếu 18:00 swing còn nguyên |
| 3 | Sau close 01:00: so sánh 2 candles trước — 08:00 mở quá xa để return về 18:00 swing? |
| 4 | Nếu có minimum objectives còn mở → 18:00 reversal valid |
| 5 | First continuation entry ngay sau 08:00 mở trên 15m/5m |

### Profile 2: 01:00 Reversal

**Điều kiện**: 18:00 range/opposing run; 01:00 tạo reversal

| Step | Action |
|------|--------|
| 1 | 18:00 candle: range hoặc opposing run |
| 2 | 01:00 candle **runs out** high hoặc low của 18:00 |
| 3 | Initial reversal confirmation trong 01:00 |
| 4 | Continuation entries trong 01:00 HOẶC 08:00 (trên 30m/15m hoặc 15m/5m) |

### Profile 3: 08:00 Reversal

**Điều kiện**: Cả 18:00 và 01:00 fail to reverse, range/opposing run

| Step | Action |
|------|--------|
| 1 | Cả 18:00 và 01:00: range hoặc opposing run |
| 2 | 08:00 candle **runs out** cả 2 opposing swings từ 18:00 và 01:00 |
| 3 | Initial reversal confirmation trong 08:00 |
| 4 | Continuation entry trong 08:00 (15m/5m) |

---

## Full Day Invalidation

Xảy ra khi 18:00 HOẶC 01:00 candle:
- Expand đến mức all objectives đã bị achieved → không còn opportunity
- Expand NGƯỢC chiều và trade through invalidation point của ngày

→ Dừng trading trong ngày đó.

---

## Previous Day Framework (Invalidation Points)

Trước khi apply profile, xác định invalidation point từ ngày hôm trước:

| Previous Day Type | Invalidation Point |
|------------------|--------------------|
| **Large Wick Day** | Equilibrium của wick (từ open đến low/high) |
| **Expansion Day** | Equilibrium của full range (low to high hoặc high to low) |
| **Hourly refinement** | Tìm opposing candles trên H1 gần invalidation point → mid-point của opposing candle series |

**Ý nghĩa**: Expansion day có small opposing wick. Intraday low (bullish) phải hình thành ABOVE invalidation point.

---

## Entry Timeframes

| Candle | Primary Timeframe | Secondary |
|--------|------------------|-----------|
| 01:00 | 30m | 15m |
| 08:00 | 15m | 5m |

> Không drop dưới 15m trong 01:00 candle. Không drop dưới 3m trong 08:00 candle.

## Related Pages

- [[7-hour-chart]] — Time windows data
- [[change-in-state-of-delivery]] — Entry confirmation mechanism
- [[expansion-model-am]] — Full methodology
