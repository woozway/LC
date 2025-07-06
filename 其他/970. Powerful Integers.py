class Solution:
  def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
    ans = set()
    for i in range(20):
      for j in range(20):
        v = x**i + y**j
        if v <= bound:
          ans.add(v)
    return ans
