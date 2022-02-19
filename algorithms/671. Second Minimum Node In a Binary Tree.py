class Solution:
  def findSecondMinimumValue(self, root: TreeNode) -> int:
    minn = root.val
    def dfs(root):
      if root is None:
        return inf
      if root.val > minn:
        return root.val
      return min(dfs(root.left), dfs(root.right))
    
    ans = dfs(root)
    return -1 if ans == inf else ans
