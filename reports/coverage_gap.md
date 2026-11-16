# Coverage-Gap Analysis Report: Bulk SMS Gateway

## 1. Timeout & Retry Boundary Conditions
- **Exact 15.0s Threshold:** Behavior when `DELIVRD` arrives simultaneously at 15,000ms as the secondary fallback triggers (race condition / duplicate SMS risk).
- **Secondary Route Timeout:** Maximum SLA timeout for the secondary fallback route is unspecified.

## 2. Malformed Payloads & SMPP Protocol Edge Cases
- **Invalid MSISDN Format:** Handling of non-E.164 recipient numbers or empty recipient lists in bulk batches.
- **Partial Batch Failure:** Behavior when 50% of a bulk batch succeeds on Primary and 50% fails over to Secondary (partial billing credit calculation).

## 3. Billing & Logging Resilience
- **Idempotency:** Ensuring duplicate DLR callbacks do not trigger multiple billing credit refunds.
- **Dead Letter Queue (DLQ):** Fallback storage if the error logging database is unreachable during a major carrier outage.
