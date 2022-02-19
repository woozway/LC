class Solution:
  def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    banset = set(banned)
    for c in "!?',;.":
      paragraph = paragraph.replace(c, ' ')
    cnt = Counter(word for word in paragraph.lower().split())
    ans, best = '', 0
    for word in cnt:
      if cnt[word] > best and word not in banset:
        ans, best = word, cnt[word]
    return ans
