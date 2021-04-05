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
        def dfs(start, end):
            if start > end: return [None, ]
            allTrees = []
            for i in range(start, end + 1):
                leftTrees = dfs(start, i - 1)
                rightTrees = dfs(i + 1, end)
                for l in leftTrees:
                    for r in rightTrees:
                        currTree = TreeNode(i)
                        currTree.left = l
                        currTree.right = r
                        allTrees.append(currTree)
            return allTrees
        
        if n < 1: return []
        return dfs(1, n)
