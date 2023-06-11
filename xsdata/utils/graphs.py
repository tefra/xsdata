from typing import Dict
from typing import Iterator
from typing import List
from typing import Set


def strongly_connected_components(edges: Dict[str, List[str]]) -> Iterator[Set[str]]:
    """
    Compute Strongly Connected Components of a directed graph.

    From https://code.activestate.com/recipes/578507/ From
    https://github.com/python/mypy/blob/master/mypy/build.py

    :param edges: Mapping of vertex-edges values
    """
    identified: Set[str] = set()
    stack: List[str] = []
    index: Dict[str, int] = {}
    boundaries: List[int] = []

    def dfs(v: str) -> Iterator[Set[str]]:
        index[v] = len(stack)
        stack.append(v)
        boundaries.append(index[v])

        for w in edges[v]:
            if w not in index:
                yield from dfs(w)
            elif w not in identified:
                while index[w] < boundaries[-1]:
                    boundaries.pop()

        if boundaries[-1] == index[v]:
            boundaries.pop()
            scc = set(stack[index[v] :])
            del stack[index[v] :]
            identified.update(scc)
            yield scc

    for vertex in set(edges):
        if vertex not in index:
            yield from dfs(vertex)
