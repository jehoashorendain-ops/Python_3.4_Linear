# Assessment 3.3: Binary Tree Traversal (BFS and DFS)
# Name: Edmer Jehoash D. Orendain

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def bfs_level_order(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        current = queue.pop(0)
        result.append(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result


def dfs_pre_order(root, result=None):
    if result is None:
        result = []
    if root:
        result.append(root.val)
        dfs_pre_order(root.left, result)
        dfs_pre_order(root.right, result)
    return result


def main():
    print("=== BINARY TREE TRAVERSAL (O, R, E, N, D, A, I, N) ===")

    # Constructing the Binary Tree nodes using letters of ORENSAIN
    # Root: O
    root = Node('O')
    root.left = Node('R')
    root.right = Node('D')
    root.left.left = Node('E')
    root.left.right = Node('N')
    root.right.left = Node('A')
    root.right.right = Node('I')
    root.left.left.left = Node('N')  # Extra leaf node for the last letter

    # BFS Traversal
    bfs_result = bfs_level_order(root)
    print(f"Breadth-First Search (BFS): {' -> '.join(bfs_result)}")

    # DFS Traversal
    dfs_result = dfs_pre_order(root)
    print(f"Depth-First Search (DFS): {' -> '.join(dfs_result)}")

    print("\nBinary Tree Traversal Complete.")


if __name__ == "__main__":
    main()