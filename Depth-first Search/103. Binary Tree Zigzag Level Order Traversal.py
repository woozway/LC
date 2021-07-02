"""
1. Clarification
2. Possible solutions
    - bfs
    - dfs
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
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        ans, queue, isOrderLeft = list(), deque([root]), True
        while queue:
            size, dq = len(queue), deque()
            for _ in range(size):
                node = queue.popleft()
                if isOrderLeft:
                    dq.append(node.val)
                else:
                    dq.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(dq)
            isOrderLeft = not isOrderLeft
        return ans


# T=O(n), S=O(n)
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans, S = list(), set()

        def dfs(node, depth):
            if not node: return
            if depth not in S:
                S.add(depth)
                ans.append([])
            ans[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        for i in range(len(ans)):
            if i % 2 == 1:
                ans[i].reverse()
        return ans
