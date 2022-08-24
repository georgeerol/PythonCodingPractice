from collections import deque


def dfs(graph, node):
    visited = []
    stack = []

    visited.append(node)
    stack.append(node)

    while stack:
        s = stack.pop()
        print(s, end=" ")
        # reverse iterate through edge list so results match recursive version
        for n in reversed(graph[s]):
            if n not in visited:
                visited.append(n)
                stack.append(n)


if __name__ == "__main__":
    g = {
        'A': ['B', 'C'],
        'B': ['D', 'E', 'F'],
        'C': ['G'],
        'D': [],
        'E': [],
        'F': ['H'],
        'G': ['I'],
        'H': [],
        'I': []
    }
    dfs(graph=g, node='A')
