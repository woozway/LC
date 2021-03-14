"""
1. Clarification
2. Possible solutions
     - Recursive
     - Iterative
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def inorder(root):
            if not root: return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        res = list()
        if not root: return res
        inorder(root)
        return res


# # T=O(n), S=O(n)
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         res = list()
#         if not root: return res
#         stack = []
#         node = root
#         while stack or node:
#             while node:
#                 stack.append(node)
#                 node = node.left
#             node = stack.pop()
#             res.append(node.val)
#             node = node.right
#         return res


# # T=O(n), S=O(1)
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         res = list()
#         if not root: return res
#         pre, node = None, root
#         while node:
#             if node.left:
#                 pre = node.left
#                 while pre.right and pre.right != node:
#                     pre = pre.right
#                 if not pre.right:
#                     pre.right = node
#                     node = node.left
#                 else:
#                     res.append(node.val)
#                     pre.right = None
#                     node = node.right
#             else:
#                 res.append(node.val)
#                 node = node.right
#         return res
