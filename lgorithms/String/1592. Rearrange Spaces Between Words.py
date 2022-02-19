class Solution:
  def reorderSpaces(self, text: str) -> str:
    spacecnt = text.count(' ')
    words = text.split()
    if len(words) == 1:
      return words[0] + ' ' * spacecnt
    quotient, remainder = divmod(spacecnt, len(words)-1)
    return (' ' * quotient).join(words)  + ' ' * remainder
