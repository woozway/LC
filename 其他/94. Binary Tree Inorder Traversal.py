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
        if not root: return []
        self.ret = []
        self.dfs(root)
        return self.ret

    def dfs(self, root):
        if not root: return
        self.dfs(root.left)
        self.ret.append(root.val)
        self.dfs(root.right)


# T=O(n), S=O(n)
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = list()
        if not root: return res
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res


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
