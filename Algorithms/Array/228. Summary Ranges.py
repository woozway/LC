class Solution:
  def summaryRanges(self, nums: List[int]) -> List[str]:
    n = len(nums)
    if n == 0:
      return []
    ans = []
    l = 0
    r = 0
    pre = nums[0]-1
    for i in range(n):
      if nums[i] == pre+1:
        r = i
      else:
        ans.append(str(nums[l])) if r == l else ans.append(str(nums[l]) + '->' + str(nums[r]))
        l = r+1
        r = l
      pre = nums[i]
    ans.append(str(nums[l])) if r == l else ans.append(str(nums[l]) + '->' + str(nums[r]))
    return ans
