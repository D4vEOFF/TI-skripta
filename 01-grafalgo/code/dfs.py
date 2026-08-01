"""Rekurzivni implementace prohledavani grafu do hloubky."""


def dfs(graph, start):
    """Vrati poradi, casy otevreni a uzavreni a DFS strom."""
    state = {vertex: "nenalezeny" for vertex in graph}
    opened = {}
    closed = {}
    parent = {vertex: None for vertex in graph}
    order = []
    time = 0

    def visit(vertex):
        nonlocal time
        state[vertex] = "otevreny"
        time += 1
        opened[vertex] = time
        order.append(vertex)

        for neighbor in graph[vertex]:
            if state[neighbor] == "nenalezeny":
                parent[neighbor] = vertex
                visit(neighbor)

        state[vertex] = "uzavreny"
        time += 1
        closed[vertex] = time

    visit(start)
    return order, opened, closed, parent


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }
    result = dfs(graph, "A")
    print("Poradi otevreni:", result[0])
    print("Casy otevreni:", result[1])
    print("Casy uzavreni:", result[2])
    print("Predchudci:", result[3])
