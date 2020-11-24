class Solution:
  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    i, j, k = 0, 0, 0
    nums = nums1[:]
    while i < m and j < n:
      if nums[i] <= nums2[j]:
        nums1[k] = nums[i]
        i, k = i+1, k+1
      else:
        nums1[k] = nums2[j]
        j, k = j+1, k+1
    while i < m:
      nums1[k] = nums[i]
      i, k = i+1, k+1
    while j < n:
      nums1[k] = nums2[j]
      j, k = j+1, k+1
