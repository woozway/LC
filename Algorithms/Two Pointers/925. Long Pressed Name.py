class Solution:
  def isLongPressedName(self, name: str, typed: str) -> bool:
    flag, j, pre = True, 0, '#'
    for c in name:
      while j < len(typed) and typed[j] != c and typed[j] == pre:
        j += 1
      if j < len(typed) and typed[j] == c:
        j += 1
      else:
        return False
      pre = c
    while j < len(typed) and typed[j] == pre:
      j += 1
    return True if flag == True and j >= len(typed) else False
