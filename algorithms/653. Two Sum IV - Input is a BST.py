class Solution:
  def findTarget(self, root: TreeNode, k: int) -> bool:
    S = set()
    def dfs(root):
      if root is None:
        return False
      if k - root.val in S:
        return True
      S.add(root.val)
      return dfs(root.left) or dfs(root.right)
    return dfs(root)
