class Solution:
  def findTilt(self, root: TreeNode) -> int:
    self.ans = 0
    def dfs(root):
      if root is None:
        return 0
      L = dfs(root.left)
      R = dfs(root.right)
      self.ans += abs(L - R)
      return L + R + root.val
    
    dfs(root)
    return self.ans
