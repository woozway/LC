class Solution:
  def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
    for a in pieces:
      if a[0] not in arr or a != arr[arr.index(a[0]):arr.index(a[0])+len(a)]:
        return False
    return True
