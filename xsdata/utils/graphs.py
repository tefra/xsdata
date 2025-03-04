from collections.abc import Iterator


def strongly_connected_components(edges: dict[str, list[str]]) -> Iterator[set[str]]:
    """Compute Strongly Connected Components of a directed graph.

    From https://code.activestate.com/recipes/578507/ From
    https://github.com/python/mypy/blob/master/mypy/build.py

    Args:
        edges: A vertex-edges map

    Yields:
        A set of the strongly connected components
    """
    identified: set[str] = set()
    stack: list[str] = []
    index: dict[str, int] = {}
    boundaries: list[int] = []

    def dfs(v: str) -> Iterator[set[str]]:
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
