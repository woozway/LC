"""
1. Clarification
2. Possible solutions
    - dfs, bottom-up
    - dfs, top-down
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
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# T=O(n), S=O(n)
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        self.MaxDep = 0
        self.dfs(root, 1)
        return self.MaxDep

    def dfs(self, root, depth):
        if not root: return
        if not root.left and not root.right:
            self.MaxDep = max(self.MaxDep, depth)
            return
        self.dfs(root.left, depth + 1)
        self.dfs(root.right, depth + 1)


# T=O(n), S=O(n)
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        Q = collections.deque()
        Q.append(root)
        ret = 0
        while Q:
            level_size = len(Q)
            for _ in range(level_size):
                node = Q.popleft()
                if node.left: Q.append(node.left)
                if node.right: Q.append(node.right)
            ret += 1
        return ret
