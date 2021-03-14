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

# # T=O(n), S=O(n)
# class Solution:
#     def postorderTraversal(self, root: TreeNode) -> List[int]:
#         if not root: return []
#         self.ret = []
#         self.dfs(root)
#         return self.ret

#     def dfs(self, root):
#         if not root: return
#         self.dfs(root.left)
#         self.dfs(root.right)
#         self.ret.append(root.val)


# T=O(n), S=O(n)
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = list()
        if not root: return res
        stack = []
        node = root
        prev = None
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if not node.right or node.right == prev:
                res.append(node.val)
                prev = node
                node = None
            else:
                stack.append(node)
                node = node.right
        return res


# # T=O(n), S=O(1)
# class Solution:
#     def postorderTraversal(self, root: TreeNode) -> List[int]:
#         def addPath(node: TreeNode):
#             count = 0
#             while node:
#                 count += 1
#                 res.append(node.val)
#                 node = node.right
#             i, j = len(res) - count, len(res) - 1
#             while i < j:
#                 res[i], res[j] = res[j], res[i]
#                 i += 1
#                 j -= 1

#         res = list()
#         if not root: return res
#         p1 = root
#         while p1:
#             p2 = p1.left
#             if p2:
#                 while p2.right and p2.right != p1:
#                     p2 = p2.right
#                 if not p2.right:
#                     p2.right = p1
#                     p1 = p1.left
#                     continue
#                 else:
#                     p2.right = None
#                     addPath(p1.left)
#             p1 = p1.right
#         addPath(root)
#         return res
