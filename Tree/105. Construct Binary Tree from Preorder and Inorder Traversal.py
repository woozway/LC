"""
1. Clarification
2. Possible solutions
 - recursion
 - iteration
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
        def helper(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right: return None
            preorder_root = preorder_left
            inorder_root = index[preorder[preorder_root]]
            root = TreeNode(preorder[preorder_root])
            size_left_subtree = inorder_root - inorder_left
            root.left = helper(preorder_left + 1, preorder_left + size_left_subtree, inorder_left, inorder_root - 1)
            root.right = helper(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1, inorder_right)
            return root

        if not preorder or not inorder or len(preorder) != len(inorder): return None
        n = len(preorder)
        index = {element: i for i, element in enumerate(inorder)}
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
