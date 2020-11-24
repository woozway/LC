class Solution:
  def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    """
    T=O(n), S=O(1)
    """
    n = len(nums)
    for i in range(n):
      new_index = abs(nums[i]) - 1
      if nums[new_index] > 0:
        nums[new_index] *= -1
    ans = []    
    for i in range(1, n+1):
      if nums[i-1] > 0:
        ans.append(i)
    return ans
