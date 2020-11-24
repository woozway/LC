class Solution:
  def findSpecialInteger(self, arr: List[int]) -> int:
    n = len(arr)
    span = n // 4 + 1
    for i in range(0, n, span):
      l = bisect.bisect_left(arr, arr[i])
      r = bisect.bisect_right(arr, arr[i])
      if r - l >= span:
        return arr[i]
    return -1
