"""
1. Clarification
2. Possible solutions
    - Recursively, bottom-up
    - Iteratively
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
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(p, q):
            if not p and not q: return True
            if not p or not q: return False
            return p.val == q.val and check(p.right, q.left) and check(p.left, q.right)

        if not root: return True
        return check(root.left, root.right)

       
# T=O(n), S=O(n)
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        Q = collections.deque([root.left, root.right])
        while Q:
            u = Q.popleft()
            v = Q.popleft()
            if not u and not v:
                continue
            if not u or not v:
                return False
            if u.val != v.val:
                return False
            [Q.append(x) for x in (u.left, v.right, u.right, v.left)]
        return True
