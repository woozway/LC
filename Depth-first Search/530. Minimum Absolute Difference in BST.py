"""
1. Clarification
2. Possible solutions
    - Inorder traversal
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
    def getMinimumDifference(self, root: TreeNode) -> int:
        if not root: return -1
        self.prev = None
        self.ans = math.inf
        self.dfs(root)
        return self.ans

    def dfs(self, root):
        if not root: return
        self.dfs(root.left)
        if self.prev:
            self.ans = min(self.ans, root.val - self.prev.val)
        self.prev = root
        self.dfs(root.right)
