class Solution:
  def readBinaryWatch(self, num: int) -> List[str]:
    def countOne(n):
      ret = 0
      while n:
        n &= n-1
        ret += 1
      return ret

    ans = []
    for i in range(12):
      for j in range(60):
        if countOne(i) + countOne(j) == num:
          ans.append(str(i) + ':' + '{:02}'.format(j))
    return ans
