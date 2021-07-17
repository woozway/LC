
"""
1. Clarification
2. Possible solutions
    - dfs
    - bfs
3. Coding
4. Tests
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# T=O(n), S=O(n)
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root: return False
        parent, depth = {}, {}

        def dfs(node, par=None):
            if node:
                depth[node.val] = 1 + depth[par.val] if par else 0
                parent[node.val] = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        return depth[x] == depth[y] and parent[x] != parent[y]


# T=O(n), S=O(n)
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root: return False
        parent, depth = {}, {}
        q = collections.deque([root])
        parent[root.val] = None
        depth[root.val] = 0
        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
                depth[node.left.val] = 1 + depth[node.val]
                parent[node.left.val] = node.val
            if node.right:
                q.append(node.right)
                depth[node.right.val] = 1 + depth[node.val]
                parent[node.right.val] = node.val
        return depth[x] == depth[y] and parent[x] != parent[y]
