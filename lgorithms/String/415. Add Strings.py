class Solution:
  def addStrings(self, num1: str, num2: str) -> str:
    ans = ''
    i, j, carry = len(num1)-1, len(num2)-1, 0
    while i >= 0 or j >= 0:
      a = ord(num1[i])-ord('0') if i >= 0 else 0
      b = ord(num2[j])-ord('0') if j >= 0 else 0
      tmp = a + b + carry
      carry = tmp // 10
      ans = str(tmp % 10) + ans
      i, j = i-1, j-1
    return '1' + ans if carry else ans
