"""
1. Clarification
2. Possible solutions
    - bfs, batch processing
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
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        ret = []
        Q = collections.deque([root])
        while Q:
            sz = len(Q)
            current_level = []
            for _ in range(sz):
                node = Q.popleft()
                current_level.append(node.val)
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            ret.append(current_level)
        return ret

       
# T=O(n), S=O(n)
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        self.result = []
        self._dfs(root, 0)
        return self.result

    def _dfs(self, node, level):
        if not node: return
        if len(self.result) < level + 1: self.result.append([])
        self.result[level].append(node.val)
        self._dfs(node.left, level + 1)
        self._dfs(node.right, level + 1)
