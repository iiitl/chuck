# ordering_core Usage

The `ordering_core` task performs large-scale sorting operations and evaluates
merge-path based ordering performance.

It is designed to benchmark how efficiently the system can sort large datasets.

## Example

Run the benchmark for the ordering task:

python -m chuck bench --task ordering_core

## Example Output

ordering_core: 0.039965s on size 250000 (count=250000)

## Explanation

- `size` / `count`: number of elements being sorted
- execution time shows how long the sorting workload took