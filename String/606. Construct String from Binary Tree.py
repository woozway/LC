class Solution:
  def tree2str(self, t: TreeNode) -> str:
    if not t:
      return ''
    if not t.left and not t.right:
      return str(t.val)
    ans = str(t.val)
    if t.left:
      ans += '(' + self.tree2str(t.left) + ')'
    else:
      ans += '()'
    if t.right:
      ans += '(' + self.tree2str(t.right) + ')'
    return ans
    
