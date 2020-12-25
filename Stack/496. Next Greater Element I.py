class Solution:
  def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    stack = []
    nextGreater = {}
    for num in nums2:
      while stack and num > stack[-1]:
        nextGreater[stack.pop()] = num
      stack.append(num)
    return [nextGreater.get(num, -1) for num in nums1]
