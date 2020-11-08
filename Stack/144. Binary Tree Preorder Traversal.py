class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
        Recursive solution is trivial, do it iteratively,
        same result if you switch left&right nodes when traversing
        """
        ans, stack = [], []
        while root or stack:
            while root:
                stack.append(root)
                ans.append(root.val)
                root = root.left
            if stack:
                root = stack.pop()
                root = root.right
        return ans
