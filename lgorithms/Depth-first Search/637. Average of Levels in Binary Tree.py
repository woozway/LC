class Solution:
  def averageOfLevels(self, root: TreeNode) -> List[float]:
    d = {}
    self.maxdepth = 0
    ans = []
    def dfs(root, depth):
      if root is None:
        return
      self.maxdepth = max(self.maxdepth, depth)
      d.setdefault(depth, []).append(root.val)
      dfs(root.left, depth+1)
      dfs(root.right, depth+1)

    dfs(root, 1)
    for i in range(1, self.maxdepth+1):
      ans.append(sum(d[i]) / len(d[i]))
    return ans
