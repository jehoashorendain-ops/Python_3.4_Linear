# Name: EDMER ORENDAIN
# Assessment 3.6: DFS Method in Tree

# Class representing a single node in the binary tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# Class representing the Binary Tree with DFS Traversal Methods
class BinaryTree:
    def __init__(self, root_val):
        self.root = Node(root_val)

    # 1. Pre-order Traversal (Root -> Left -> Right)
    def dfs_pre_order(self, node, result=None):
        if result is None:
            result = []
        if node:
            result.append(node.val)
            self.dfs_pre_order(node.left, result)
            self.dfs_pre_order(node.right, result)
        return result

    # 2. In-order Traversal (Left -> Root -> Right)
    def dfs_in_order(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.dfs_in_order(node.left, result)
            result.append(node.val)
            self.dfs_in_order(node.right, result)
        return result

    # 3. Post-order Traversal (Left -> Right -> Root)
    def dfs_post_order(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.dfs_post_order(node.left, result)
            self.dfs_post_order(node.right, result)
            result.append(node.val)
        return result


# Driver code to demonstrate DFS methods using letters from EDMER ORENDAIN
if __name__ == "__main__":
    # Constructing the binary tree using letters from EDMER ORENDAIN:
    #         O
    #       /   \
    #      R     E
    #     / \   / \
    #    N   D A   M

    tree = BinaryTree('O')
    tree.root.left = Node('R')
    tree.root.right = Node('E')
    tree.root.left.left = Node('N')
    tree.root.left.right = Node('D')
    tree.root.right.left = Node('A')
    tree.root.right.right = Node('M')

    print("--- Depth-First Search (DFS) Tree Traversals ---")
    print("Student Name: EDMER ORENDAIN")
    print("Pre-order Traversal (Root → Left → Right):  ", " → ".join(tree.dfs_pre_order(tree.root)))
    print("In-order Traversal (Left → Root → Right):   ", " → ".join(tree.dfs_in_order(tree.root)))
    print("Post-order Traversal (Left → Right → Root): ", " → ".join(tree.dfs_post_order(tree.root)))