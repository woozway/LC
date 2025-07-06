class Solution:
  def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
    start, end = rounds[0], rounds[-1]
    if start <= end:
      return list(range(start, end + 1))
    else:
      leftPart = range(1, end + 1)
      rightPart = range(start, n + 1)
      return list(itertools.chain(leftPart, rightPart))
