class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        c = collections.Counter((A + ' ' + B).split())
        return [k for k, v in c.items() if v == 1]
