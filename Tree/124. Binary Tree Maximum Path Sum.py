"""
1. Clarification
2. Possible solutions
    - Recursive, bottom-up
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
    def __init__(self):
        self.maxSum = -math.inf

    def maxPathSum(self, root: TreeNode) -> int:
        def maxGain(node):
            if not node:
                return 0
            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)
            self.maxSum = max(self.maxSum, node.val + leftGain + rightGain)
            return node.val + max(leftGain, rightGain)

        maxGain(root)
        return self.maxSum
