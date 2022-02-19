class Solution:
  def largeGroupPositions(self, s: str) -> List[List[int]]:
    cnt = 0
    firstIndex = 0
    pre = '#'
    s += '#'
    ans = []
    for i in range(len(s)):
      if s[i] != pre:
        if cnt >= 3:
          ans.append([firstIndex, i-1])
        cnt = 1
        firstIndex = i
      else:
        cnt += 1
      pre = s[i]
    return ans
