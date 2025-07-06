class Solution:
  def sumNumbers(self, root: TreeNode) -> int:
    def dfs(root: TreeNode, prevTotal: int) -> int:
      if not root:
        return 0
      total = prevTotal * 10 + root.val
      if not root.left and not root.right:
        return total
      else:
        return dfs(root.left, total) + dfs(root.right, total)
    return dfs(root, 0)
