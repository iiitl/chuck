from __future__ import annotations

from random import Random
from typing import Any

from ...common import TaskSpec
import numpy as np


def generate(size: int, seed: int) -> dict[str, Any]:
    rng = Random(seed)
    left = [[rng.randrange(0, 10) for _ in range(size)] for _ in range(size)]
    right = [[rng.randrange(0, 10) for _ in range(size)] for _ in range(size)]
    return {"left": left, "right": right, "block_size": max(2, min(16, size // 4 or 2))}


def solve(payload: dict[str, Any]) -> dict[str, Any]:
    left = np.array(payload["left"])
    right = np.array(payload["right"])
    size = len(left)
    result = np.matmul(left, right)
    trace = int(np.trace(result))
    checksum = int(np.sum(result))
    return {"size": size, "trace": trace, "checksum": checksum}


TASK_SPEC = TaskSpec("compute_core", generate, solve, 16, 64)
