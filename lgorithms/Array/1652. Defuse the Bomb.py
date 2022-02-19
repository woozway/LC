class Solution:
  def decrypt(self, code: List[int], k: int) -> List[int]:
    n = len(code)
    ans = [0]*n
    for i in range(n):
      for j in range(abs(k)):
        ans[i] += code[(i+1+j)%n] if k > 0 else code[(i-1-j+n)%n]
    return ans
