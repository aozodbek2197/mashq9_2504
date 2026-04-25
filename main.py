from collections import deque
from typing import Dict, List

class Graph:
    def __init__(self) -> None:
        self.adj: Dict[int, List[int]] = {}

    def add_edge(self, u: int, v: int) -> None:
        self.adj.setdefault(u, []).append(v)
        self.adj.setdefault(v, []).append(u)

    def bfs(self, start: int) -> List[int]:
        visited = set()
        queue = deque([start])
        order = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                order.append(node)
                queue.extend(self.adj.get(node, []))

        return order


if __name__ == "__main__":
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)

    print(g.bfs(1))
