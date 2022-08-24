from collections import deque


def bfs(graph, node):
    visited = []
    queue = deque()

    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.popleft()
        print(s, end=" ")

        for n in graph[s]:
            if n not in visited:
                visited.append(n)
                queue.append(n)


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
    bfs(graph=g, node='A')
