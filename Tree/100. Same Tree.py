"""
1. Clarification
2. Possible solutions
    - Recursion
    - Iteration
3. Coding
4. Tests
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# T=O(n), S=O(lgn)
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q: return True
        if not q or not p: return False
        if p.val != q.val: return False
        return self.isSameTree(p.right, q.right) and \
               self.isSameTree(p.left, q.left)


# T=O(n), S=O(lgn)
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def check(p, q):
            if not p and not q: return True
            if not q or not p: return False
            if p.val != q.val: return False
            return True

        deq = collections.deque([(p, q), ])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False
            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
        return True
