from collections import defaultdict
from contextlib import contextmanager
from time import perf_counter_ns


@contextmanager
def stopwatch(name: str):
    """Simple context manager that logs elapsed times."""
    start_time = perf_counter_ns()
    yield
    stop_time = perf_counter_ns()
    stopwatches[name].append(stop_time - start_time)


stopwatches: dict[str, list[int]] = defaultdict(list)
