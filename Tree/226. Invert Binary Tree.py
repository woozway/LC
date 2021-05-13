"""
1. Clarification
2. Possible solutions
    - Recursive
    - Iterative
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
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return root
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root


# T=O(n), S=O(n)
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return root
        q = collections.deque([root])
        while q:
            cur = q.popleft()
            cur.left, cur.right = cur.right, cur.left
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return root
