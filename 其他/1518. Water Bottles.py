class Solution:
  def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
    cnt = numBottles
    while numBottles >= numExchange:
      cnt += 1
      numBottles = numBottles - numExchange + 1
    return cnt
