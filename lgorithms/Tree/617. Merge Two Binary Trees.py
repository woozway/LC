"""
1. Clarification
2. Possible solutions
    - Recursive, dfs
    - Iterative, bfs
3. Coding
4. Tests
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# T=O(min(m,n)), S=O(min(m,n))
class Solution:
    def mergeTrees(self, rooroot1: TreeNode, rooroot2: TreeNode) -> TreeNode:
        if not rooroot1:
            return rooroot2
        if not rooroot2:
            return rooroot1
        merged = TreeNode(rooroot1.val + rooroot2.val)
        merged.left = self.mergeTrees(rooroot1.left, rooroot2.left)
        merged.right = self.mergeTrees(rooroot1.right, rooroot2.right)
        return merged


# T=O(min(m,n)), S=O(min(m,n))
from collections import deque

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1: return root2
        if not root2: return root1

        merged = TreeNode(root1.val + root2.val)
        q, q1, q2 = deque([merged]), deque([root1]), deque([root2])
        while q1 and q2:
            node, node1, node2 = q.popleft(), q1.popleft(), q2.popleft()
            left_root1, right_root1 = node1.left, node1.right
            left_root2, right_root2 = node2.left, node2.right
            if left_root1 or left_root2:
                if left_root1 and left_root2:
                    left = TreeNode(left_root1.val + left_root2.val)
                    node.left = left
                    q.append(left)
                    q1.append(left_root1)
                    q2.append(left_root2)
                elif left_root1:
                    node.left = left_root1
                elif left_root2:
                    node.left = left_root2
            if right_root1 or right_root2:
                if right_root1 and right_root2:
                    right = TreeNode(right_root1.val + right_root2.val)
                    node.right = right
                    q.append(right)
                    q1.append(right_root1)
                    q2.append(right_root2)
                elif right_root1:
                    node.right = right_root1
                elif right_root2:
                    node.right = right_root2

        return merged
