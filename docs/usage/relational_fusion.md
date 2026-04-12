# relational_fusion — Usage Guide

`relational_fusion` performs a hash-join on two relations (left and right) and
computes aggregated summary values over the joined rows. It mirrors a common
database execution strategy: build a hash index on one side, stream the other,
and aggregate on the fly.

---

## Quick CLI usage

```bash
# benchmark all tasks (relational_fusion included)
python -m chuck bench

# benchmark only relational_fusion
python -m chuck bench --task relational_fusion

# run regression checks (validates relational_fusion against stored baselines)
python -m chuck regress
```

---

## Using the Python API directly

### Generate input data

`generate(row_count, seed)` creates a synthetic workload of two relations.

```python
from chuck.tasks.relational_fusion import generate

payload = generate(row_count=128, seed=42)
print(type(payload))
# <class 'dict'>
print(payload.keys())
# dict_keys(['left', 'right'])
```

#### Example input (truncated)

```python
{
    "left": [
        ("k007", 26),
        ("k017", 251),
        ("k014", 143),
        # ... 128 rows total
    ],
    "right": [
        ("k028", 144),
        ("k027", 188),
        ("k017", 474),
        # ... 64 rows total (max(4, row_count // 2))
    ],
}
```

Each row is a `(key, value)` tuple. Keys are strings like `"k005"`, and values
are random integers in `[1, 999]`.

---

### Solve

`solve(payload)` performs the join + aggregation and returns summary statistics.

```python
from chuck.tasks.relational_fusion import generate, solve

payload = generate(row_count=128, seed=42)
result = solve(payload)
print(result)
```

#### Example output

```python
{
    "left_rows": 128,
    "right_rows": 64,
    "join_rows": 269,
    "aggregate": 273329,
}
```

| Field | Description |
|---|---|
| `left_rows` | Number of rows in the left relation |
| `right_rows` | Number of rows in the right relation |
| `join_rows` | Total number of rows produced by the inner join |
| `aggregate` | Sum of `(left_value + right_value)` across all joined row pairs |

---

## End-to-end example script

```python
"""relational_fusion end-to-end demo."""

from chuck.tasks.relational_fusion import generate, solve

# 1. Generate a workload
payload = generate(row_count=128, seed=10)
print(f"Left rows  : {len(payload['left'])}")
print(f"Right rows : {len(payload['right'])}")

# 2. Solve
result = solve(payload)
print(f"Join rows  : {result['join_rows']}")
print(f"Aggregate  : {result['aggregate']}")

# 3. Verify against the known regression baseline (seed=10, size=128)
assert result == {
    "left_rows": 128,
    "right_rows": 64,
    "join_rows": 269,
    "aggregate": 276559,
}
print("✓ Output matches regression baseline")
```

**Expected terminal output:**

```
Left rows  : 128
Right rows : 64
Join rows  : 269
Aggregate  : 276559
✓ Output matches regression baseline
```

---

## Benchmarking

```python
from chuck.benchmarks.relational_fusion import run

result = run()
print(f"Task    : {result['task']}")
print(f"Size    : {result['size']}")
print(f"Seconds : {result['seconds']}")
print(f"Output  : {result['output']}")
```

The benchmark uses `row_count=40_000` (the task's `benchmark_size`) by default,
giving a realistic workload for performance measurement.

---

## How the algorithm works

1. **Index the right relation** — build a `dict[str, list[int]]` mapping each
   key to the list of values on the right side.
2. **Stream the left relation** — for every `(key, left_value)` in the left
   table, look up matching right-side values via the hash index.
3. **Aggregate** — for each matched pair, increment `join_rows` and accumulate
   `left_value + right_value` into `aggregate`.

This is a classic hash-join followed by an inline aggregation, equivalent to:

```sql
SELECT COUNT(*)        AS join_rows,
       SUM(l.val + r.val) AS aggregate
FROM   left_table  l
JOIN   right_table r ON l.key = r.key;
```

---

## Native C++ backend

If the C++ native module is built, `chuck` will automatically use it for faster
execution. The algorithm is identical; only the runtime differs.

```bash
# build native modules (Linux / macOS / WSL2)
python scripts/setup_native.py

# benchmark with explicit backend selection
python -m chuck snapshot --label cpp_run --backend cpp
python -m chuck snapshot --label py_run  --backend python

# compare
python -m chuck compare \
    --old data/reports/snapshots/py_run.json \
    --new data/reports/snapshots/cpp_run.json
```

See [NATIVE_BINDINGS.md](../NATIVE_BINDINGS.md) for build details.
