"""
1. Clarification
2. Possible solutions
    - Recursive, top-down v1
    - Recursive, top-down v2
    - Iterative: if you reverse inorder traversal sequence of a tree,
                 (which is [root.left, root, root.right]), you get 
                 reversed inorder traversal sequence, (which is 
                 [root.right, root, root.left]); if you reverse postorder 
                 traversal seq (which is [root.left, root.right, root]), 
                 you'll get reversed preorder trav seq of that tree, (
                 which is [root, root.right, root.left])
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
        def helper(in_left, in_right, post_left, post_right):
            if in_left > in_right: return None
            rootVal = postorder[post_right]
            node = TreeNode(rootVal)
            in_idx = val2idx[rootVal]
            leftCnt = in_idx - in_left
            node.left = helper(in_left, in_idx - 1, post_left, post_left + leftCnt - 1)
            node.right = helper(in_idx + 1, in_right, post_left + leftCnt, post_right - 1)
            return node

        if not inorder or not postorder or len(inorder) != len(postorder): return None
        val2idx = {val: idx for idx, val in enumerate(inorder)}
        n = len(inorder)
        return helper(0, n - 1, 0, n - 1)


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
