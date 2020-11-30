class Solution:
  def toGoatLatin(self, S: str) -> str:
    def convert(word):
      if not re.match("[aeiouAEIOU]", word[0]):
        word = word[1:] + word[:1]
      return word + 'ma'
    return ' '.join(convert(word) + 'a'*i for i, word in enumerate(S.split(), 1))
