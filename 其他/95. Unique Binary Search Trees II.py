"""
1. Clarification
2. Possible solutions
    - Recursion
3. Coding
4. Tests
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# T=O(4^n/(n^1/2)), S=O(4^n/(n^1/2))
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n < 1: return []
        return self.dfs(1, n)
    
    def dfs(self, start, end):
        if start > end: return [None, ]
        allTree = []
        for i in range(start, end + 1):
            leftTree = self.dfs(start, i - 1)
            rightTree = self.dfs(i + 1, end)
            for l in leftTree:
                for r in rightTree:
                    node = TreeNode(i)
                    node.left = l
                    node.right = r
                    allTree.append(node)
        return allTree
