"""
1. Clarification
2. Possible solutions
    - Recursive
    - Iterative
3. Coding
4. Tests
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# T=O(h), S=O(h)
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root or root.val == val: return root
        return self.searchBST(root.left, val) if val < root.val else self.searchBST(root.right, val)


# T=O(h), S=O(1)
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root or root.val == val: return root
        while root and root.val != val:
            root = root.left if val < root.val else root.right
        return root
