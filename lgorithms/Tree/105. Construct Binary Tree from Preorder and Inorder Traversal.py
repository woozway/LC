"""
1. Clarification
2. Possible solutions
    - Recursive, top-down
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(in_left, in_right, pre_left, pre_right):
            if in_left > in_right: return None
            rootVal = preorder[pre_left]
            node = TreeNode(rootVal)
            in_idx = val2idx[rootVal]
            leftCnt = in_idx - in_left
            node.left = helper(in_left, in_idx - 1, pre_left + 1, pre_left + 1 + leftCnt - 1)
            node.right = helper(in_idx + 1, in_right, pre_left + leftCnt + 1, pre_right)
            return node

        if not preorder or not inorder or len(preorder) != len(inorder): return None
        n = len(preorder)
        val2idx = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, n - 1, 0, n - 1)


# # T=O(n), S=O(n)
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         if not preorder or not inorder or len(preorder) != len(inorder): return None
#         root = TreeNode(preorder[0])
#         stack = [root]
#         inorderIndex = 0
#         for i in range(1, len(preorder)):
#             preorderVal = preorder[i]
#             node = stack[-1]
#             if node.val != inorder[inorderIndex]:
#                 node.left = TreeNode(preorderVal)
#                 stack.append(node.left)
#             else:
#                 while stack and stack[-1].val == inorder[inorderIndex]:
#                     node = stack.pop()
#                     inorderIndex += 1
#                 node.right = TreeNode(preorderVal)
#                 stack.append(node.right)
#         return root
