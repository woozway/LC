"""
1. Clarification
2. Possible solutions
 - dfs, bottom-up
 - dfs, top-down
 - bfs
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
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# # T=O(n), S=O(n)
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if not root: return 0
#         self.MaxDep = 0
#         self.dfs(root, 1)
#         return self.MaxDep
#
#     def dfs(self, root, depth):
#         if not root: return
#         if not root.left and not root.right:
#             self.MaxDep = max(self.MaxDep, depth)
#             return
#         self.dfs(root.left, depth + 1)
#         self.dfs(root.right, depth + 1)


# # T=O(n), S=O(n)
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if not root: return 0
#         queue = collections.deque()
#         queue.append(root)
#         ret = 0
#         while queue:
#             level_size = len(queue)
#             for _ in range(level_size):
#                 node = queue.popleft()
#                 if node.left: queue.append(node.left)
#                 if node.right: queue.append(node.right)
#             ret += 1
#         return ret
