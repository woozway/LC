"""
1. Clarification
2. Possible solutions
    - In-Order Traversal
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
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root: return None
        self.ans, self.cur = None, None
        self.dfs(root)
        return self.ans

    def dfs(self, node):
        if not node: return
        self.dfs(node.left)
        if not self.cur:
            self.ans = TreeNode(node.val)
            self.cur = self.ans
        else:
            self.cur.right = TreeNode(node.val)
            self.cur = self.cur.right
        self.dfs(node.right)
