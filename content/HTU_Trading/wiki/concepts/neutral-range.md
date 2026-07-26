---
type: concept
title: "Neutral Range"
tags: [range-type, structure, caution, swing, medium]
related: [failure-swings, protected-swings, expansion-model-am, the-market-lens-2025-expansion-model]
created: 2026-05-07
updated: 2026-05-07
---

# Neutral Range

**Definition**: Điều kiện thị trường khi failure swings hình thành cả 2 phía VÀ giá đã trade về equilibrium của 2 failure swings đó — không có hướng trade rõ ràng.

**Source**: [[the-market-lens-2025-expansion-model]] — Section 3: Caution Protocol

---

## Điều kiện để gọi là Neutral Range

Cả 2 điều kiện phải xảy ra:
1. **Failure swings cả 2 phía** (failure swing highs AND failure swing lows)
2. **Price đã trade về equilibrium** của 2 failure swing extremes

→ Lúc này neither side of the market can be traded away from.

## Daily Timeframe Signal

Neutral range thường bắt đầu với **inside daily candle** — không có protected swing từ ngày trước ở bất kỳ phía nào.

> Internal ranges chỉ trade khi market đang trade off một previously established reversal. Nếu thiếu context đó → không trade within previous day's range.

---

## Kiểm tra False Failure Swings trước

**Bắt buộc** so sánh correlated pair trước khi accept là true neutral range:

| Kết quả so sánh | Hành động |
|----------------|----------|
| Cả 2 pairs có failure swings | → True neutral range → áp dụng Neutral Range Protocol |
| Một pair có manipulation (divergence) | → False failure swings → thực ra là directional → trade divergence |

---

## Neutral Range Protocol

1. Mark out: **Highest high** và **Lowest low** của failure swings (creating the range)
2. Chờ giá engage với một trong 2 extremes
3. Tại extreme đó:

**Scenario A: Manipulation xảy ra**
- Shallow run từ daily open → trade intraday với daily profile confirmation
- Extended run từ daily open → confirm, trade TIẾP THEO với daily candle là continuation ngược hướng

**Scenario B: Continuation (không có manipulation)**
- Daily candle close ABOVE highest high hoặc BELOW lowest low
- Xác nhận: hourly opposing close candles đã bị close through
- Close through này tạo protected swing trong continuation cho ngày tiếp theo
- Thường là ngày tiếp theo thay vì same day

---

## Phân biệt với External/Internal Range

| Range Type | Đặc điểm | Trade Away From |
|-----------|---------|----------------|
| **External Range** | Price tại failure swing extreme ở một phía | Yes — sau manipulation/divergence |
| **Internal Range** | Price trong range, đã có confirmed reversal | Yes — continuation of reversal |
| **Neutral Range** | Failure swings cả 2 phía + EQ reached | No — chờ protocol tại extremes |

## Related Pages

- [[failure-swings]] — Neutral range được định nghĩa bởi failure swings cả 2 phía
- [[protected-swings]] — Protected swing cần hình thành mới có thể trade neutral range
- [[expansion-model-am]] — Methodology context
