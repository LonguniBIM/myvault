---
type: concept
title: "Protected Swings"
tags: [swing, structure, invalidation, execution, high]
related: [failure-swings, change-in-state-of-delivery, expansion-model-am, the-market-lens-2025-expansion-model]
created: 2026-05-07
updated: 2026-05-07
---

# Protected Swings

**Definition**: Điểm giá có thể trade away từ theo hướng ngược lại — được bảo vệ bởi manipulation hoặc divergence đã được confirmed.

**Source**: [[the-market-lens-2025-expansion-model]] — Section 2: Price Signatures

---

## Hình thành qua 2 cơ chế

### 1. Manipulation (cơ chế chính)

**Bullish manipulation** (protected low):
1. Giá chạy qua (trade below) relevant low
2. Giá return nhanh về trên (quickly returns above)
3. **Confirmation**: Close above the opening price of the highest downclose candle that ran into the low
4. → Low đó giờ là protected swing

**Bearish manipulation** (protected high):
1. Giá chạy qua (trade above) relevant high
2. Giá return nhanh về dưới (quickly returns below)
3. **Confirmation**: Close below the opening price of the lowest upclose candle that ran into the high
4. → High đó giờ là protected swing

> Manipulation chỉ là anticipation trước khi có confirmation. SAU confirmation mới là actionable signature.

### 2. Divergence (khi correlated pair có failure swing)

**Divergence low** (trên pair có failure swing):
- Confirmation: Close above open của highest downclose candle forming the higher low
- Protected swing = Lower low (failure swing low) — vẫn còn intact cho đến khi trade through

**Divergence high** (trên pair có failure swing):
- Confirmation: Close below open của lowest upclose candle forming the lower high
- Protected swing = Higher high (failure swing high)

**Optional extra confirmation**: Chờ CISD trên cả 2 correlated pairs để có highest quality confirmation.

---

## Invalidation Rules

| Scope | Invalidation |
|-------|-------------|
| **HTF Framework** | Close through 50% level của highest body to lowest body trong opposing candle series |
| **Entry (stop loss)** | Trade through the protected swing point itself |

> Never place stop internally within opposing candles. Stop ALWAYS ở bên kia protected swing point.

---

## Opposing Candles trong Continuation

Sau khi protected swing confirmed, opposing close candles được sử dụng để:
1. Support price trong continuation (downclose candles support bullish; upclose candles resist bearish)
2. Trail stop loss (close through bulky opposing candles = new invalidation)

**Selection criteria cho opposing candles hợp lệ**:
- Single candle hoặc series với **bulky body** + **wide range**
- **Invalid**: Small range candle body/wick → không expected để price respect

---

## Opposing Candles dùng như Framework

| Scenario | Invalidation |
|---------|-------------|
| HTF framework (xác định bias) | Close through 50% của candle body series |
| Entry (LTF confirmation) | Trade through protected swing point |

---

## Ứng dụng

- Mọi trade opportunity đều cần protected swing → không có protected swing = không có valid framework
- Opposing draw (failure swings ở phía đối diện) = ideal objective
- Continuation trades từ confirmed protected swing ngày trước là "easiest" framework

## Related Pages

- [[failure-swings]] — Failure swings là nơi protected swings hình thành
- [[change-in-state-of-delivery]] — CISD là confirmation cho protected swing
- [[expansion-model-am]] — Methodology context
