class Solution:
  def videoStitching(self, clips: List[List[int]], T: int) -> int:
    index, cnt, maxn = 0, 0, 0
    while index < T:
      flag = 0
      for l in clips:
        if l[0] <= index:
          tmp = maxn
          maxn = max(maxn, l[1])
          if maxn != tmp:
            flag = 1
      if flag == 0:
        return -1
      else:
        index = maxn
        cnt += 1
    return cnt
