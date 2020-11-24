class Solution:
  def arrayPairSum(self, nums: List[int]) -> int:
    """
    T=O(n), S=O(n)
    """
    d = [0]*20001
    for i in range(len(nums)):
      d[nums[i]+10000] += 1
    i, j, ans = 0, 0, 0
    while i < 20001:
      if d[i]:
        if j%2 == 0:
          ans += i-10000
        d[i] -= 1
        j += 1
      else:
        i += 1
    return ans
