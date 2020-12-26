class KthLargest:
  
  def __init__(self, k: int, nums: List[int]):
    self._nums = nums
    heapq.heapify(self._nums)
    self._k = k
    while len(self._nums) > k:
      heapq.heappop(self._nums)

  def add(self, val: int) -> int:
    if len(self._nums) < self._k:
      heapq.heappush(self._nums, val)
    elif val > self._nums[0]:
      heapq.heapreplace(self._nums, val)
    return self._nums[0]
