class Solution:
  def specialArray(self, nums: List[int]) -> int:
    """
    T=O(n), S=O(n)
    """
    n = len(nums)
    cnt = [0]*(n+1)
    for x in nums:
      cnt[min(x, n)] += 1
    for i in range(n,-1,-1):
      if i < n:
        cnt[i] += cnt[i+1]
      if cnt[i] == i:
        return i
    return -1
