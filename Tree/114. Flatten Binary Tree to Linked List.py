"""
1. Clarification
2. Possible solutions
    - Preorder, resursive
    - Preorder, iterative
    - Preorder v3
    - Search for prenode
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
    def flatten(self, root: TreeNode) -> None:
        preorderList = list()
        def preorderTraversal(node):
            if node:
                preorderList.append(node)
                preorderTraversal(node.left)
                preorderTraversal(node.right)

        preorderTraversal(root)
        for i in range(1, len(preorderList)):
            prev, curr = preorderList[i-1], preorderList[i]
            prev.left, prev.right = None, curr


# T=O(n), S=O(n)
class Solution:
    def flatten(self, root: TreeNode) -> None:
        preorderList = list()
        stack = list()
        node = root
        while node or stack:
            while node:
                preorderList.append(node)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        for i in range(1, len(preorderList)):
            prev, curr = preorderList[i-1], preorderList[i]
            prev.left, prev.right = None, curr


# T=O(n), S=O(n)
class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return
        stack = [root]
        prev = None
        while stack:
            curr = stack.pop()
            if prev:
                prev.left = None
                prev.right = curr
            left, right = curr.left, curr.right
            if right:
                stack.append(right)
            if left:
                stack.append(left)
            prev = curr


# T=O(n), S=O(1)
class Solution:
    def flatten(self, root: TreeNode) -> None:
        curr = root
        while curr:
            if curr.left:
                predecessor = nxt = curr.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = curr.right
                curr.left = None
                curr.right = nxt
            curr = curr.right
