class Solution:
  def reformatNumber(self, number: str) -> str:
    s = number.replace('-', '').replace(' ', '')
    ans = []
    while True:
      if len(s) > 4:
        ans.append(s[:3])
        s = s[3:]
      elif len(s) == 4:
        ans.append(s[:2])
        ans.append(s[2:])
        break
      else:
        ans.append(s[:])
        break
    return '-'.join(ans)
