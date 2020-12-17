class Solution:
  def isBalanced(self, root: TreeNode) -> bool:
    def height(root):
      return 0 if not root else max(height(root.left), height(root.right)) + 1

    return True if not root else abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
