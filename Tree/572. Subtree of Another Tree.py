class Solution:
  
  def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
    
    def check(o, t):
      if not o and not t:
        return True
      if (o and not t) or (not o and t) or (o.val != t.val):
        return False
      return check(o.left, t.left) and check(o.right, t.right)
    
    def dfs(o, t):
      if o is None:
        return False
      return check(o, t) or dfs(o.left, t) or dfs(o.right, t)

    return dfs(s, t)
