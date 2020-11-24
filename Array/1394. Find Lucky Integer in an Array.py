class Solution:
  def findLucky(self, arr: List[int]) -> int:
    freq = Counter(arr)
    ans = [k for k in freq if k == freq[k]]
    return max(ans) if len(ans) else -1
