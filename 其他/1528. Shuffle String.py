class Solution:
  def restoreString(self, s: str, indices: List[int]) -> str:
    ans = [''] * len(indices)
    for idx, v in enumerate(indices):
      ans[v] = s[idx]
    return ''.join(ans)
