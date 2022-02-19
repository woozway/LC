class Solution:
  def reformat(self, s: str) -> str:
    digits = findall(r'\d', s)
    chars = findall(r'[a-z]', s)
    if abs(len(digits)-len(chars)) > 1: return ''
    shorter, longer = sorted([digits, chars], key=len)
    return ''.join(map(''.join, zip_longest(longer, shorter, fillvalue='')))
