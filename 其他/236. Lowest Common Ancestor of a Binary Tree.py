"""
1. Clarification
2. Possible solutions
    - Find common node leave-to-root (not likely node with parent pointer)
    - Since vals are unique, find path1 & path2, then output the last common node
    - Recursive, bottom-up (can be used in BST too)
3. Coding
4. Tests
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# T=O(n), S=O(n)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p1, self.p2 = [], []
        self.findpath(self.p1, [], root, p)
        self.findpath(self.p2, [], root, q)
        return self.lca()

    def findpath(self, path, tmppath, root, node):
        if root is None: return
        tmppath.append(root)
        if root == node:
            path.extend(tmppath)
            tmppath.pop()
            return
        self.findpath(path, tmppath, root.left, node)
        self.findpath(path, tmppath, root.right, node)
        tmppath.pop()

    def lca(self):
        S = set(self.p2)
        ans = None
        for p in self.p1:
            if p in S:
                ans = p
        return ans


# T=O(n), S=O(n)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q): return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left or right
