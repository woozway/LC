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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(in_left, in_right):
            if in_left > in_right: return None
            val = postorder.pop()
            root = TreeNode(val)
            index = val2idx[val]
            root.right = helper(index + 1, in_right)
            root.left = helper(in_left, index - 1)
            return root

        if not inorder or not postorder or len(inorder) != len(postorder): return None
        val2idx = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)

       
# T=O(n), S=O(n)
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder or len(inorder) != len(postorder): return None
        root = TreeNode(postorder[-1])
        stack = [root]
        inorderIndex = len(inorder) - 1
        for i in range(len(postorder) - 2, -1, -1):
            postorderVal = postorder[i]
            node = stack[-1]
            if node.val != inorder[inorderIndex]:
                node.right = TreeNode(postorderVal)
                stack.append(node.right)
            else:
                while stack and stack[-1].val == inorder[inorderIndex]:
                    node = stack.pop()
                    inorderIndex -= 1
                node.left = TreeNode(postorderVal)
                stack.append(node.left)
        return root
