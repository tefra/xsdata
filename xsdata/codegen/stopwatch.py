from collections import defaultdict
from contextlib import contextmanager
from time import perf_counter_ns
from typing import Dict, List


@contextmanager
def stopwatch(name: str):
    """Simple context manager that logs elapsed times."""
    start_time = perf_counter_ns()
    yield
    stop_time = perf_counter_ns()
    stopwatches[name].append(stop_time - start_time)


stopwatches: Dict[str, List[int]] = defaultdict(list)
