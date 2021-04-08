"""
1. Clarification
2. Possible solutions
    - bfs
    - dfs + top-down
    - dfs + bottom-up
3. Coding
4. Tests
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# T=O(n), S=O(n)
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        Q = collections.deque([root])
        depth = 0
        while Q:
            sz = len(Q)
            depth += 1
            for _ in range(sz):
                node = Q.popleft()
                Q.extend(node.children)
        return depth


# T=O(n), S=O(n)
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        self.MaxDep = 0
        self.dfs(root, 1)
        return self.MaxDep

    def dfs(self, node, depth):
        if not node: return
        if not node.children:
            self.MaxDep = max(self.MaxDep, depth)
            return
        for child in node.children:
            self.dfs(child, depth + 1)


# T=O(n), S=O(n)
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        if not root.children: return 1
        return 1 + max(self.maxDepth(child) for child in root.children)
