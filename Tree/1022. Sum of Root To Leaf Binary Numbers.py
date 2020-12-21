class Solution:
  def sumRootToLeaf(self, root: TreeNode) -> int:
    self.ans = 0
    s = []
    def dfs(node):
      if node:
        s.append(str(node.val))
        if not node.left and not node.right:
          self.ans += int(''.join(s), 2)
          s.pop()
          return
        dfs(node.left)
        dfs(node.right)
        s.pop()
    
    dfs(root)
    return self.ans
