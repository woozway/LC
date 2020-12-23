class Solution:
  def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    """ decorator in python3.x really is a black magic! """
    m = {}
    st = set(wordDict)
    @lru_cache(None)
    def backtrack(s, index):
      if not s in m:
        if index == len(s):
          m[index] = ['']
          return
        m[index] = []
        for i in range(index+1, len(s)+1):
          w = s[index:i]
          if w in st:
            backtrack(s, i)
            for j in m[i]:
              m[index].append(w if j=='' else w+' '+j)
    backtrack(s, 0)
    return m[0]
