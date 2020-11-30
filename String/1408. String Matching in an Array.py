class Solution:
  def stringMatching(self, words: List[str]) -> List[str]:
    return [s for s in words if any(w != s and s in w for w in words)]
