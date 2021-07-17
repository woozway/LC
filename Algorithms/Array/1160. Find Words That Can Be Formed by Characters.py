class Solution:
  def countCharacters(self, words: List[str], chars: str) -> int:
    chars_cnt = Counter(chars)
    ans = 0
    for word in words:
      word_cnt = Counter(word)
      for c in word_cnt:
        if chars_cnt[c] < word_cnt[c]:
          break
      else:
        ans += len(word)
    return ans
