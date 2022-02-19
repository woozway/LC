class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        S1 = set('qwertyuiop')
        S2 = set('asdfghjkl')
        S3 = set('zxcvbnm')
        ans = []
        for word in words:
            s = set(word.lower())
            if s <= S1 or s <= S2 or s <= S3:
                ans.append(word)
        return ans
