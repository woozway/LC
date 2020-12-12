class Solution:
  def constructRectangle(self, area: int) -> List[int]:
    sqrt = area ** 0.5
    for W in range(int(sqrt), 0, -1):
      if area % W == 0:
        return [area//W, W]
