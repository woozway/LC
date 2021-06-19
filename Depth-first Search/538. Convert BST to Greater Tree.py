"""
1. Clarification
2. Possible solutions
    - Inorder tree traversal v1
    - Inorder tree traversal v2
    - Morris traversal
3. Coding
4. Tests
"""


# T=O(n), S=O(n)
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(root: TreeNode):
            nonlocal total
            if root:
                dfs(root.right)
                total += root.val
                root.val = total
                dfs(root.left)

        total = 0
        dfs(root)
        return root


# T=O(n), S=O(n)
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        nodes = list()
        def dfs(node):
            if not node: return
            dfs(node.left)
            nodes.append(node)
            dfs(node.right)

        dfs(root)
        runningSum = 0
        for i in range(len(nodes) - 1, -1, -1):
            runningSum += nodes[i].val
            nodes[i].val = runningSum
        return root


# T=O(n), S=O(1)
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def getSuccessor(node: TreeNode) -> TreeNode:
            succ = node.right
            while succ.left and succ.left != node:
                succ = succ.left
            return succ

        total = 0
        node = root
        while node:
            if not node.right:
                total += node.val
                node.val = total
                node = node.left
            else:
                succ = getSuccessor(node)
                if not succ.left:
                    succ.left = node
                    node = node.right
                else:
                    succ.left = None
                    total += node.val
                    node.val = total
                    node = node.left
        return root
