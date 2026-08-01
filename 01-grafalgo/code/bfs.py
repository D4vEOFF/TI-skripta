"""Jednoducha implementace prohledavani grafu do sirky."""

from collections import deque


def bfs(graph, start):
    """Vrati vzdalenosti a predchudce vrcholu dosazitelnych ze startu."""
    distance = {vertex: None for vertex in graph}
    parent = {vertex: None for vertex in graph}
    queue = deque([start])
    distance[start] = 0

    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if distance[neighbor] is None:
                distance[neighbor] = distance[vertex] + 1
                parent[neighbor] = vertex
                queue.append(neighbor)

    return distance, parent


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }
    distances, parents = bfs(graph, "A")
    print("Vzdalenosti:", distances)
    print("Predchudci:", parents)
