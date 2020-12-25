class Solution:
  def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    stack, ans = [], []
    d = {}
    for num in nums2:
      while stack and num > stack[-1]:
        d[stack.pop()] = num
      stack.append(num)
    while stack:
      d[stack.pop()] = -1
    for num in nums1:
      ans.append(d[num])
    return ans
