class Solution:
  def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs: return ''
    s1 = min(strs)
    s2 = max(strs)
    for idx, ch in enumerate(s1):
      if ch != s2[idx]:
        return s2[:idx]
    return s1
