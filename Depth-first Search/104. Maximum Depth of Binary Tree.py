"""
1. Clarification
2. Possible solutions
 - dfs
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
