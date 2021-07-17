class Solution:
  def reverseOnlyLetters(self, S: str) -> str:
    letters = [c for c in S if c.isalpha()]
    ans = []
    for c in S:
      ans.append(letters.pop() if c.isalpha() else c)
    return ''.join(ans)
