"""
1. Clarification
2. Possible solutions
 - check whether inorder sequence is increasing
 - recursion, max(left subtree) < root && min(right substree) > root
3. Coding
4. Tests
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# T=O(n), S=O(1)
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.prev = None
        return self.inorder(root)

    def inorder(self, root):
        if root is None: return True
        if not self.inorder(root.left): return False
        if self.prev and self.prev.val >= root.val: return False
        self.prev = root
        return self.inorder(root.right)

# # T=O(n), S=O(n)
# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         return self.isValid(root, None, None)

#     def isValid(self, root, minn, maxn):
#         if root is None: return True
#         if minn is not None and root.val <= minn: return False
#         if maxn is not None and root.val >= maxn: return False
#         return self.isValid(root.left, minn, root.val) and self.isValid(root.right, root.val, maxn)
