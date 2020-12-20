class Solution:
  def postorder(self, root: 'Node') -> List[int]:
    """ do it iteratively """
    if root is None:
      return []
    stack, ans = [root, ], []
    while stack:
      root = stack.pop()
      if root is not None:
        ans.append(root.val)
      for c in root.children:
        stack.append(c)
    return ans[::-1]
