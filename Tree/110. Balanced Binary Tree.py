"""
1. Clarification
2. Possible solutions
 - top-down recursive
 - bottom-up recursive
3. Coding
4. Tests
"""


# # T=O(n^2), S=O(n)
# class Solution:
#     def isBalanced(self, root: TreeNode) -> bool:
#         def height(root: TreeNode) -> int:
#             if not root: return 0
#             return max(height(root.left), height(root.right)) + 1
#
#         if not root: return True
#         return abs(height(root.left) - height(root.right)) <= 1 \
#                and self.isBalanced(root.left) and self.isBalanced(root.right)


# T=O(n), S=O(n)
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root: return 0
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            else:
                return max(leftHeight, rightHeight) + 1

        if not root: return True
        return height(root) >= 0
