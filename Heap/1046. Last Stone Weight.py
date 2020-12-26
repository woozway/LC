class Solution:
  def lastStoneWeight(self, stones: List[int]) -> int:
    darkStones = [-1 * s for s in stones]
    heapify(darkStones)
    while True:
      if not darkStones:
        return 0
      elif len(darkStones) == 1:
        return -darkStones[0]
      else:
        a = heappop(darkStones)
        b = heappop(darkStones)
        if a != b:
          heappush(darkStones, a-b)
