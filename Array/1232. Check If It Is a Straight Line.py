class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
      c = coordinates[:]
      n = len(coordinates)
      for i in range(2, n):
        if (c[1][1]-c[0][1]) * (c[i][0]-c[i-1][0]) != (c[i][1]-c[i-1][1]) * (c[1][0]-c[0][0]):
          return False
      return True
