class Solution:
  def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
    for index, word in enumerate(sentence.split(), 1):
      if word.startswith(searchWord):
        return index
    else:
      return -1
