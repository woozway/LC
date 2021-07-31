"""
1. Clarification
2. Possible solutions
    - Backtracking, tree
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
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def backtrack(node):
            if not node:
                return
            tmplist.append(node.val)
            if not node.left and not node.right:
                if sum(tmplist) == targetSum:
                    ans.append(tmplist[:])
                tmplist.pop()
                return
            backtrack(node.left)
            backtrack(node.right)
            tmplist.pop()
        
        ans, tmplist = list(), list()
        backtrack(root)
        return ans
