class Solution:
  def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
    tot = 0
    acc = [0]*len(distance)
    for i, x in enumerate(distance):
      tot += x
      if i != 0:
        acc[i] = acc[i-1] + distance[i-1]
    a, b = sorted([start, destination])
    diff = acc[b] - acc[a]
    return min(diff, tot-diff)
