"""
1. Clarification
2. Possible solutions
    - dfs, top-down
    - bfs
3. Coding
4. Tests
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# T=O(n), S=O(h)
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root: return False
        if not root.left and not root.right: return targetSum == root.val
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)


# T=O(n), S=O(h)
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root: return False
        Q_node = collections.deque([root])
        Q_val = collections.deque([root.val])
        while Q_node:
            node = Q_node.popleft()
            Sum = Q_val.popleft()
            if not node.left and not node.right:
                if Sum == targetSum:
                    return True
                continue
            if node.left:
                Q_node.append(node.left)
                Q_val.append(node.left.val + Sum)
            if node.right:
                Q_node.append(node.right)
                Q_val.append(node.right.val + Sum)
        return False
