class Solution:
  def minDiffInBST(self, root: TreeNode) -> int:
    seq = []
    def dfs(root):
      if root is None:
        return
      dfs(root.left)
      seq.append(root.val)
      dfs(root.right)
    
    dfs(root)
    return min(seq[i]-seq[i-1] for i in range(1, len(seq)))
