class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        s = [c.upper() for c in S if c != '-']
        s.reverse()
        cnt = 0
        ans = ''
        for i, c in enumerate(s):
            ans += c
            cnt += 1
            if cnt % K == 0 and i != len(s) - 1:
                ans += '-'
        return ans[::-1]
