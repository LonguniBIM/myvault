---
type: concept
title: "Change in State of Delivery (CISD)"
tags: [execution, signature, structure, high]
related: [protected-swings, daily-profiles, expansion-model-am, the-market-lens-2025-expansion-model]
created: 2026-05-07
updated: 2026-05-07
---

# Change in State of Delivery (CISD)

**Definition**: Confirmation signal cho manipulation hoặc reversal — xác nhận khi nào protected swing đã formed và có thể trade.

**Source**: [[the-market-lens-2025-expansion-model]] — Section 2 & 5

---

## Định nghĩa

CISD là sự thay đổi trong "trạng thái phân phối" của giá — từ bearish delivery sang bullish (hoặc ngược lại), được xác nhận bằng một close cụ thể qua opposing candles.

---

## CISD cho Manipulation

**Bullish (confirm protected low)**:
> Close ABOVE the **opening price** of the **highest downclose candle** trong series that ran into the low

**Bearish (confirm protected high)**:
> Close BELOW the **opening price** of the **lowest upclose candle** trong series that ran into the high

*Trước CISD: manipulation chỉ là anticipation. Sau CISD: actionable signal.*

---

## CISD cho Divergence

**Divergence low (trên pair có failure swing)**:
> Close above opening price của **highest downclose candle** forming the higher low

**Divergence high (trên pair có failure swing)**:
> Close below opening price của **lowest upclose candle** forming the lower high

---

## CISD cho Initial Reversal Intraday (Daily Profile)

**Bullish daily profile reversal**:
> Close above lowest downclose candles tại vùng intraday low — in respect to previous day invalidation point

**Bearish daily profile reversal**:
> Close below highest upclose candles tại vùng intraday high

---

## CISD cho Opposing Candles trong Continuation

Khi trong continuation và gặp series opposing candles:
- Bullish: close above open của highest downclose candle trong series
- Bearish: close below open của lowest upclose candle trong series

---

## 50% Rule (Respecting / Invalidation)

Sau khi CISD confirmed, series opposing candles được "respected" khi:
- **Bullish**: Price ở trên 50% level của highest body to lowest body trong downclose series
- **Bearish**: Price ở dưới 50% level của highest body to lowest body trong upclose series

Vi phạm 50% rule ở HTF = framework invalid.

---

## Timeframe Pairings (Fractal Model reference)

| Higher TF Swing | CISD Confirmation |
|----------------|------------------|
| Weekly | 4H CISD |
| Daily | 1H CISD |
| 4H | 15m CISD |
| 1H | 5m CISD |
| 30m | 3m CISD |
| 15m | 1m CISD |

---

## Key Rules

1. Candle được chọn = **bulky body + wide range** (không phải small doji/small wick)
2. Entry = market order ngay khi **close through** — không chờ retest
3. Stop loss = swing point **bên kia** opposing candles (không internal)

## Related Pages

- [[protected-swings]] — CISD là confirmation cho protected swing
- [[daily-profiles]] — CISD applied để confirm intraday reversal
- [[expansion-model-am]] — Full methodology
