---
type: concept
title: "Expansion Rule"
tags: [caution, structure, day-trading, swing, high]
related: [daily-profiles, expansion-model-am, failure-swings, the-market-lens-2025-expansion-model]
created: 2026-05-07
updated: 2026-05-07
---

# Expansion Rule

**Definition**: Trigger để dừng trading continuations — xảy ra khi có 3 consecutive expansion daily candles cùng hướng. Đánh dấu kết thúc một phase of expansion.

**Source**: [[the-market-lens-2025-expansion-model]] — Section 3: Caution Protocol

---

## Điều kiện kích hoạt

3 daily candles LIÊN TIẾP cùng hướng, và mỗi candle phải là **true expansion candle**:

| Yêu cầu | Chi tiết |
|---------|---------|
| **Larger than average range** | Range lớn hơn trung bình so với recent candles |
| **Bulky candle body** | Body chiếm phần lớn candle → holding trend trong candle |

> Không phải mọi daily close cùng hướng đều count. Candle phải là visual expansion, không phải doji hay inside bar.

---

## Hành động khi Expansion Rule kích hoạt

1. **Dừng trade continuations** theo hướng cũ ngay lập tức
2. **Anticipate new phase of price delivery** — thường là reversal hoặc consolidation
3. **Cho phép thêm ngày in** để xác định bias mới
4. Sử dụng **protected swings** để xác định hướng phase tiếp theo

## Trong Weekly Range

**Weekly logic tương tự**: No weekly profile calls for more than 3 consecutive expansion days in same direction within one week. Understanding expansion rule = understanding weekly profiles.

---

## Daily Expansion Cycle

```
Expansion → New Phase of Price → Expansion → ...
           (Reversal / Consolidation / Retracement)
```

Sau Expansion Rule: market "cần" hình thành lại và đưa giá về một phase trung gian trước khi expansion tiếp theo.

## Monday Rule (liên quan)

Vào đầu tuần mới: bias từ tuần trước KHÔNG được carry over. Monday là ngày không trade để allow weekly narrative to establish → tránh bị trapped trong bias của phase cũ.

## Related Pages

- [[daily-profiles]] — Profile alignment trong một ngày expansion
- [[expansion-model-am]] — Full methodology context
- [[failure-swings]] — Sau expansion rule, failure swings ở phía đối diện trở thành relevant
