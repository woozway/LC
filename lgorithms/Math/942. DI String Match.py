class Solution:
  def diStringMatch(self, S: str) -> List[int]:
    low, high = 0, len(S)
    ans = []
    for x in S:
      if x == 'I':
        ans.append(low)
        low += 1
      else:
        ans.append(high)
        high -= 1
    return ans + [low]
