"""
1. Clarification
2. Possible solutions
 - recursive
 - iterative
 - Morris traversal
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
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preorder(root: TreeNode):
            if not root: return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)

        res = list()
        preorder(root)
        return res


# # T=O(n), S=O(n)
# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         res = list()
#         if not root: return res
#         stack = []
#         node = root
#         while stack or node:
#             while node:
#                 res.append(node.val)
#                 stack.append(node)
#                 node = node.left
#             node = stack.pop()
#             node = node.right
#         return res


# # T=O(n), S=O(1)
# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         res = list()
#         if not root: return res
#         p1 = root
#         while p1:
#             p2 = p1.left
#             if p2:
#                 while p2.right and p2.right != p1:
#                     p2 = p2.right
#                 if not p2.right:
#                     res.append(p1.val)
#                     p2.right = p1
#                     p1 = p1.left
#                     continue
#                 else:
#                     p2.right = None
#             else:
#                 res.append(p1.val)
#             p1 = p1.right
#         return res
