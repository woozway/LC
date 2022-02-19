class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        valid = [ch.lower() for ch in licensePlate if ch.isalpha()]
        c = collections.Counter(valid)
        ans = []
        for word in words:
            tmpCounter = collections.Counter(word)
            for k, v in c.items():
                if k not in tmpCounter or v > tmpCounter[k]:
                    break
            else:
                ans.append(word)
        ans.sort(key=len)
        return ans[0]
