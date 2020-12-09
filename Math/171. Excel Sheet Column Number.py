class Solution:
  def titleToNumber(self, s: str) -> int:
    ans = 0
    for ch in s:
      ans *= 26
      ans += ord(ch)-ord('A')+1
    return ans
