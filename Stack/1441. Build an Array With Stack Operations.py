class Solution:
  def buildArray(self, target: List[int], n: int) -> List[str]:
    j, ans = 0, []
    for i in range(1, n+1):
      if j >= len(target):
        break
      else:
        if target[j] == i:
          ans.append('Push')
          j += 1
        elif target[j] > i:
          ans.extend(['Push', 'Pop'])
    return ans
