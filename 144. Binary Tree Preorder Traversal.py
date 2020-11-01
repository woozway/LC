class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        ans = []
        while stack:
            tmp = stack.pop()
            ans.append(tmp.val)            
            if tmp.right:
                stack.append(tmp.right)
            if tmp.left:
                stack.append(tmp.left)
        return ans
