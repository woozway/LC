"""
1. Clarification
2. Possible solutions
    - bfs + Queue
    - Recursive
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
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        res = []
        Q = collections.deque([root])
        while Q:
            sz, tmp = len(Q), []
            for i in range(sz):
                node = Q.popleft()
                tmp.append(node.val)
                Q.extend(node.children)
            res.append(tmp)
        return res


# T=O(n), S=O(n)
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        self.res = []
        if not root: return []
        self.dfs(root, 0)
        return self.res

    def dfs(self, node, level):
        if len(self.res) == level:
            self.res.append([])
        self.res[level].append(node.val)
        for child in node.children:
            self.dfs(child, level + 1)
