class Solution:
  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    a, b = Counter(ransomNote), Counter(magazine)
    return True if a & b == a else False
