class Solution:
  def lengthOfLastWord(self, s: str) -> int:
    words = s.split()
    return 0 if not words else len(words[-1])
