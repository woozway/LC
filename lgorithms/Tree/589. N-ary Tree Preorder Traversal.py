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
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        self.ans = []
        self.dfs(root)
        return self.ans

    def dfs(self, root):
        if not root: return
        self.ans.append(root.val)
        for child in root.children:
            self.dfs(child)


# T=O(n), S=O(n)
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        stack, ans = [root], []
        while stack:
            root = stack.pop()
            ans.append(root.val)
            stack.extend(root.children[::-1])
        return ans
