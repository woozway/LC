class Solution:
  def increasingBST(self, root: TreeNode) -> TreeNode:
    def dfs(node):
      if node:
        dfs(node.left)
        node.left = None
        self.cur.right = node
        self.cur = node
        dfs(node.right)

    ans = self.cur = TreeNode()
    dfs(root)
    return ans.right
