# Assessment 3.3: Graph Traversal (BFS and DFS)
# Name: Edmer Jehoash D. Orendain

from collections import deque


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, u, v):
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)  # Undirected graph

    def bfs(self, start_node):
        visited = set()
        queue = deque([start_node])
        traversal_order = []

        visited.add(start_node)
        while queue:
            node = queue.popleft()
            traversal_order.append(node)

            for neighbor in self.adjacency_list.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return traversal_order

    def dfs(self, start_node):
        visited = set()
        traversal_order = []

        def _dfs_recursive(node):
            visited.add(node)
            traversal_order.append(node)
            for neighbor in self.adjacency_list.get(node, []):
                if neighbor not in visited:
                    _dfs_recursive(neighbor)

        _dfs_recursive(start_node)
        return traversal_order


def main():
    print("=== GRAPH TRAVERSAL (O, R, E, N, D, A, I, N) ===")

    g = Graph()
    # Connecting the letters of ORENSAIN as a graph network
    edges = [
        ('O', 'R'), ('O', 'E'),
        ('R', 'N'), ('R', 'D'),
        ('E', 'A'), ('D', 'I'),
        ('A', 'N')
    ]

    for u, v in edges:
        g.add_edge(u, v)

    start_vertex = 'O'

    bfs_result = g.bfs(start_vertex)
    print(f"Graph BFS Traversal: {' -> '.join(bfs_result)}")

    dfs_result = g.dfs(start_vertex)
    print(f"Graph DFS Traversal: {' -> '.join(dfs_result)}")

    print("\nGraph Traversal Complete.")


if __name__ == "__main__":
    main()