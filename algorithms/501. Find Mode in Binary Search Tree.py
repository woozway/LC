class Solution:
  def findMode(self, root: TreeNode) -> List[int]:
    d = {}
    def dfs(root):
      if root is None:
        return
      d[root.val] = d.get(root.val, 0)+1
      dfs(root.left)
      dfs(root.right)
    
    dfs(root)
    maxcnt = max([0] + [v for v in d.values()])
    ans = []
    for k, v in d.items():
      if v == maxcnt:
        ans.append(k)
    return ans
