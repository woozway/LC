class Solution:
  def sumOfLeftLeaves(self, root: TreeNode) -> int:
    Sum = 0
    def dfs(root, indicator):
      if root is None:
        return
      if not root.left and not root.right:
        if indicator == 'l':
          nonlocal Sum
          Sum += root.val
        return
      dfs(root.left, 'l')
      dfs(root.right, 'r')
    
    dfs(root, 'r')
    return Sum
