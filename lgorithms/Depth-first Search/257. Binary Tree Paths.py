class Solution:
  def binaryTreePaths(self, root: TreeNode) -> List[str]:
    ans, path = [], []
    def dfs(root):
      if not root: return
      path.append(root.val)
      if not root.left and not root.right:
        ans.append('->'.join(str(x) for x in path))
        path.pop()
        return
      dfs(root.left)
      dfs(root.right)
      path.pop()
    
    dfs(root)
    return ans
