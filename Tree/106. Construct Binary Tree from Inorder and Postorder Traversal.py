"""
1. Clarification
2. Possible solutions
 - recursion
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(in_left, in_right):
            if in_left > in_right: return None
            val = postorder.pop()
            root = TreeNode(val)
            index = val2idx[val]
            root.right = helper(index + 1, in_right)
            root.left = helper(in_left, index - 1)
            return root

        if not inorder or not postorder or len(inorder) != len(postorder): return None
        val2idx = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)
