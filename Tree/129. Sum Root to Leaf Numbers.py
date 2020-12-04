class Solution:
  def sumNumbers(self, root: TreeNode) -> int:
    self.res = 0
    def dfs(node, psum):
      if not node:
        return None
      if not node.left and not node.right:
        self.res += 10*psum + node.val
        return
      psum = 10*psum + node.val
      dfs(node.left, psum)
      dfs(node.right, psum)
    dfs(root, 0)
    return self.res
