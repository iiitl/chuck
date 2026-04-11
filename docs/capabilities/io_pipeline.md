# io_pipeline

What it does: Reads many line records, transforms them, and computes totals.

Algorithm design:
- Parse each record in one pass.
- Group by `(account, bucket)` and sum amounts.
- Track the top pair using a running max.

Why this design:
- Single-pass aggregation keeps memory and time predictable.
- Good fit for stream-like IO workloads.

Input: Line records shaped like `account|bucket|amount`.

Output: `records`, `groups`, `top_pair`, `top_value`, `checksum`.

## Usage Example


```python
from chuck.tasks.io_pipeline.task import generate, solve


sample_records = generate(count=1000, seed=42)
print(f"Generated {len(sample_records)} pipeline records.")
print(f"Sample record: {sample_records[0]}")


result = solve(records=sample_records)


print("\nPipeline Results:")
print(f"Records Processed: {result['records']}")
print(f"Unique Account/Bucket Pairs: {result['unique_pairs']}")
print(f"Total Value Aggregated: {result['total_value']}")
print(f"Top Pair: {result['top_pair']} (Value: {result['top_value']})")