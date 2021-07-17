class Solution:
  def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    i, cnt = 0, 0
    m = len(flowerbed)
    while i < m:
      if flowerbed[i]==0 and (i==0 or flowerbed[i-1]==0) and (i==m-1 or flowerbed[i+1]==0):
        flowerbed[i] = 1
        i += 1
        cnt += 1
      if cnt >= n:
        return True
      i += 1
    return False
