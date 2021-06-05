"""
1. Clarification
2. Possible solutions
    - Brute force
    - Memoization
3. Coding
4. Tests
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# T=O(n^2), S=O(n)
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.cnt = 0
        self.dfs(root, targetSum)
        return self.cnt

    def dfs(self, node, target):
        if node is None: return
        self.test(node, target)
        self.dfs(node.left, target)
        self.dfs(node.right, target)

    def test(self, node, target):
        if node is None: return
        if node.val == target: self.cnt += 1
        self.test(node.left, target - node.val)
        self.test(node.right, target - node.val)


# T=O(n), S=O(n)
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.result = 0
        cache = {0: 1}
        self.dfs(root, targetSum, 0, cache)
        return self.result

    def dfs(self, root, target, currPathSum, cache):
        if root is None: return
        currPathSum += root.val
        oldPathSum = currPathSum - target
        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)
        cache[currPathSum] -= 1
