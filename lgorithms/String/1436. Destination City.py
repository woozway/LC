class Solution:
  def destCity(self, paths: List[List[str]]) -> str:
    return (set(p[1] for p in paths) - set(p[0] for p in paths)).pop()
