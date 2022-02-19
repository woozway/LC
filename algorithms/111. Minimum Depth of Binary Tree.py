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

# T=O(n), S=O(h)
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        if not root.left: return 1 + self.minDepth(root.right)
        if not root.right: return 1 + self.minDepth(root.left)
        leftMinDepth = self.minDepth(root.left)
        rightMinDepth = self.minDepth(root.right)
        return 1 + min(leftMinDepth, rightMinDepth)

# # T=O(n), S=O(n)
# class Solution:
#     def minDepth(self, root: TreeNode) -> int:
#         if not root: return 0
#         queue = collections.deque([(root, 1)])
#         while queue:
#             node, depth = queue.popleft()
#             if not node.left and not node.right: return depth
#             if node.left: queue.append((node.left, depth + 1))
#             if node.right: queue.append((node.right, depth + 1))
