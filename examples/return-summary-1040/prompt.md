# Example: 1040 return summary

User prompt for the `return-summary-1040` skill:

```
Use return-summary-1040. Here are the 2024 Form 1040 highlights:

- Filing status: MFJ; 2 dependents
- Total income (Line 9): $215,000
- AGI (Line 11): $208,000
- Standard deduction (Line 12): $29,200
- QBI deduction (Line 13): $0 (couple is above threshold; SSTB
  full disqualification — TI > $483,900? Wait, TI = $208K - $29.2K
  = $178.8K, below threshold; QBI was missed by preparer. Flag.)
- Taxable income (Line 15): $178,800
- Tax (Line 16): $26,832
- Total tax (Line 24): $26,832
- Total payments (Line 33): $28,500
- Refund (Line 34): $1,668

Schedule C: net profit $215,000 (CPA solo practice, accounting,
SSTB).
Schedule B: $4,000 of interest income; foreign accounts box not
checked.

Question: Summarize the return and flag any planning issues.
```

Expected output: see `expected-output.json`.
