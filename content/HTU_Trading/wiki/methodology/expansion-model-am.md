---
type: methodology
title: "Expansion Model — AM (The Market Lens)"
tags: [strategy, caution, structure, invalidation, execution, killzone, swing, range-type, expansion, bias, signature, objective, day-trading, high]
related: [failure-swings, protected-swings, neutral-range, daily-profiles, expansion-rule, change-in-state-of-delivery, 7-hour-chart, the-market-lens-2025-expansion-model, extract-the-market-lens-expansion-flow]
created: 2026-05-07
updated: 2026-05-07
skill_status: candidate
invalidation_complete: true
layers_covered: [caution, structure, invalidation, execution]
---

# Expansion Model — AM (The Market Lens)

**Source**: [[the-market-lens-2025-expansion-model]]

**Author**: AM / The Market Lens

**Core Thesis**: Mọi ngày expansion trên thị trường đều có thể được anticipate, confirm, và execute thông qua 4-layer filter: Caution → Structure → Invalidation → Execution. Hệ thống cung cấp clear invalidation ở mỗi lớp → không cần đoán mò.

---

## Layer 1: Caution Protocol

*Xác định khi nào KHÔNG trade — lọc các điều kiện unfavorable trước khi nhìn vào chart.*

### Absolute Skip Days

| Condition | Rule |
|-----------|------|
| **Monday** | Không bao giờ trade. Không có high-impact news, range nhỏ nhất tuần, không có weekly context |
| **Expansion Rule Active** | 3 consecutive expansion daily candles cùng hướng → dừng continuation trades, chờ phase mới |

### News Protocol

| Timing | Rule |
|--------|------|
| Trước high-impact news (cùng ngày) | Không mở lệnh bất kỳ session nào trước khi news ra |
| Đang giữ lệnh | Đóng tất cả TRƯỚC khi news release |
| Sau news ra | Entry bình thường được phép |
| High-impact events | CPI M/M, Non-Farm Payroll, FOMC Press Conference |

> Day prior to high-impact news: không cần tránh (data shows chỉ 7% below-average range)

---

## Layer 2: Structure

*Xác định valid framework — cần có điểm để trade away from và điểm để trade into.*

### Step 1: 30-Day Lookback

- Chỉ nhìn lại **30 daily candles** cho framework. Ngoài window này chỉ dùng làm objectives
- TradingView shortcut: Shift + drag từ current daily candle sang trái, đếm -30 bars

### Step 2: Identify Relevant Swings

Trên Daily và Hourly timeframes:
1. Tìm **failure swings** — extremes mà thị trường failed to reverse properly
2. **Kiểm tra correlated pair**: False failure swing = correlated pair có manipulation → thực ra là directional
3. Relevant swing = highest high (bearish) hoặc lowest low (bullish) trong series

### Step 3: Classify Range

| Range Type | Condition | Action |
|-----------|---------|--------|
| **External Range** | Price tại failure swing extreme một phía | Frame reversal nếu manipulation/divergence xảy ra |
| **Internal Range** | Price trong range, có confirmed reversal từ trước | Trade continuation |
| **Neutral Range** | Failure swings cả 2 phía + price tại EQ | Apply [[neutral-range]] protocol |

### Step 4: Find Valid Framework

Một trong 3 scenarios:

**A) Close Proximity Swing**: Daily mở gần failure swing → frame reversal at that level. Manipulation + small daily wick = ideal expansion setup. Có thể trade reversal day hoặc wait for reversal + trade continuation next day.

**B) Confirmed Protected Swing**: Previous day confirmed reversal + opposing objective còn mở → trade continuation. Tiếp tục đến khi objective đạt hoặc expansion rule kích hoạt.

**C) Opposing Draw**: Failure swings ở phía đối diện = ideal objective. Less resistance along the way.

---

## Layer 3: Invalidation

*Xác định chính xác điểm nào invalidate idea TRƯỚC khi trade.*

### HTF Framework Invalidation

Close through **50% level** của highest body to lowest body trong opposing candle series → framework no longer valid manipulation.

*Bullish: price phải stay above 50% downclose candles; Bearish: stay below 50% upclose candles*

### Entry Invalidation (Stop Loss)

Trade through **protected swing point** (manipulation low khi bullish; manipulation high khi bearish).

> Không bao giờ đặt stop INTERNAL trong opposing candles. Stop LUÔN ở ngoài protected swing point.

### Previous Day Invalidation Point

| Previous Day | Invalidation |
|-------------|-------------|
| Large Wick Day | Equilibrium của wick (open to low/high) |
| Expansion Day | Equilibrium của full range (low to high hoặc ngược) |
| Hourly refinement | Opposing candles trên H1 gần invalidation → midpoint của series |

*Intraday reversal phải hình thành ABOVE invalidation point (bullish) hoặc BELOW (bearish)*

### Day Invalidation

Nếu 18:00 hoặc 01:00 candle expand significantly:
- All objectives taken out → không còn opportunity → skip day
- Expand ngược chiều qua invalidation point → skip day

---

## Layer 4: Execution

*Confirm entry và execute với đúng timeframe, signature, và risk management.*

### Step 1: Daily Profile Selection

Xác định profile dựa trên cách 7H candles develop:

| Profile | 18:00 candle | 01:00 candle | Entry Window |
|---------|-------------|-------------|-------------|
| **18:00 Reversal** | Forms opposing swing | Swing intact → no trade | First entry after 08:00 open |
| **01:00 Reversal** | Range / opposing run | Runs out 18:00 + reversal confirms | Within 01:00 or 08:00 |
| **08:00 Reversal** | Range / opposing run | Range / opposing run | Within 08:00 only |

### Step 2: Initial Reversal Confirmation (CISD)

| Candle | Timeframes | Signal |
|--------|-----------|--------|
| 01:00 | 30m, 15m | Close above highest downclose (bullish) / below lowest upclose (bearish) |
| 08:00 | 15m, 5m | Same logic |

### Step 3: Continuation Entry

Sau khi initial reversal confirmed, tìm continuation entry:

- **Signal**: Close through opposing candles — bulky body, wide range, clear close
- **Confluences** (demand ít nhất 1–2): Run on short-term swing + divergence at opposing swing + opposing candle at news time + close through at news time
- **Execution**: **Market order** ngay khi close through. KHÔNG dùng limit order
- **Stop loss**: Swing point bên kia opposing candles (protected swing)

### Step 4: Objectives và Trade Management

**Objectives**:
1. Previous highs/lows trên D/4H/1H (trong 30-day lookback)
2. Equilibrium của large ranges trên D/4H/1H

**Scaling**:
- Scale 50%+ tại first objective beyond **2R**
- **KHÔNG bao giờ** để 2R+ profit thành breakeven hoặc loss

**Trailing Stop**:
- Chỉ bắt đầu manage sau **1.5R**
- Trail sử dụng opposing candles (bulky) trên 15m/5m
- Nếu giá expand aggressively (không có opposing candles): ưu tiên scale hơn trail

**Risk Rules**:
- Fixed **dollar** risk (không fixed points)
- **Max 2 losses** per day — hard rule

---

## Decision Tree (Rapid Reference)

```
Is it Monday? → SKIP
High-impact news this session (before release)? → SKIP
3 consecutive expansion days? → STOP continuations, reestablish bias

↓ Market open

30-day lookback → Identify failure swings → Check correlated pair for false signals
↓
Classify range: External / Internal / Neutral
↓ (if Neutral → Neutral Range Protocol)
Find valid framework: Close Proximity / Confirmed Swing / Continuation
Mark invalidation point from previous day

↓ Intraday

18:00 candle closes → Read context (opposing swing? range?)
No trade within 18:00

01:00 opens:
  If 18:00 had opposing swing → wait, no trade until 08:00 confirms too far to return
  If 18:00 ranged/opposing run → wait for 01:00 to run out 18:00 swing → look for CISD (30m/15m)
  
08:00 opens:
  Entry ngay sau open nếu profile valid (30m/15m hoặc 15m/5m)
  If 18:00 + 01:00 both failed → wait for 08:00 reversal (15m/5m)

↓ Entry

Market order on close through opposing candles
Stop loss = protected swing point
Trail after 1.5R, scale at 2R+
Max 2 losses per day
```

---

## Skill Build Checklist

- [x] Group A (Timing): Complete — Monday rule, news protocol, expansion rule, killzone windows
- [x] Group B (Structure): Complete — Failure swings, protected swings, range types, framework
- [x] Group C (Invalidation): Complete — 50% rule HTF, protected swing point entry, previous day EQ, day invalidation
- [x] Group D (Execution): Complete — Daily profiles, CISD, continuation entry, objectives, risk management
- [x] Decision tree: Can be expressed as If/Then flow
- [x] Invalidation: Red clearly defined (50% body rule + protected swing point)
- [x] Confirmation: Green clearly defined (CISD + close through opposing candles)
- [x] Context: Yellow (30-day framework, daily profile, correlated pairs)

**→ Ready for Skill build: `skill_status: candidate`, `invalidation_complete: true`**
