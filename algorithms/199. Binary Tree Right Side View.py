# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# T=O(n), S=O(n)
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []

        ans, trace = [], {}
        def dfs(node, height):
            if not node: return
            if height not in trace: ans.append(node.val)
            trace[height] = node.val
            dfs(node.right, height + 1)
            dfs(node.left, height + 1)

        dfs(root, 1)
        return ans


# T=O(n), S=O(n)
from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        rightmost_value_at_depth = dict()
        max_depth = -1
        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()
            if node is not None:
                max_depth = max(max_depth, depth)
                rightmost_value_at_depth[depth] = node.val
                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))
        return [rightmost_value_at_depth[depth] for depth in range(max_depth + 1)]
