class Solution:
  def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
    m = len(nums)
    n = len(nums[0])
    if m * n != r * c:
      return nums
    ori = [nums[i][j] for i in range(m) for j in range(n)]
    ans = []
    for i in range(0, len(ori), c):
      ans.append(ori[i:i+c])
    return ans
