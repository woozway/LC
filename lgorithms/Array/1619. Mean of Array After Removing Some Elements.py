class Solution:
  def trimMean(self, arr: List[int]) -> float:
    n = len(arr)
    arr.sort()
    l = int(0.05 * n)
    r = n - l
    return sum(arr[l:r]) / (r-l)
