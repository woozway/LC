class Solution:
  def isPathCrossing(self, path: str) -> bool:
    dirs = {
      'N': (0, 1),
      'S': (0, -1),
      'W': (-1, 0),
      'E': (1, 0),
    }
    x, y = 0, 0
    vis = set([(x, y)])
    for ch in path:
      dx, dy = dirs[ch]
      x, y = x + dx, y + dy
      if (x, y) in vis:
        return True
      vis.add((x, y))
    return False
