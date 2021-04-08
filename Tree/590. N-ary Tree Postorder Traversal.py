"""
1. Clarification
2. Possible solutions
    - Recursively
    - Iteratively
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
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        self.res = []
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root: return
        for child in root.children:
            self.dfs(child)
        self.res.append(root.val)


# T=O(n), S=O(n)
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        stack, res = [root, ], []
        while stack:
            root = stack.pop()
            if root is not None:
                res.append(root.val)
            stack.extend(root.children)
        return res[::-1]
