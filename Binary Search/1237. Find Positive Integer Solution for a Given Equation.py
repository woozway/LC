class Solution:
  def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
    ans, x, y = [], 1, 1000
    while x <= 1000 and y >= 1:
      tmp = customfunction.f(x, y)
      if tmp < z:
        x += 1
      elif tmp > z:
        y -= 1
      else:
        ans.append([x, y])
        x += 1
        y -= 1
    return ans
