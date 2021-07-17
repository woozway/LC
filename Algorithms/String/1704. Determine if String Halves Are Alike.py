class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        a, b = s[:n//2], s[n//2:]
        vowels = set('aeiouAEIOU')
        return sum(1 for c in a if c in vowels) == sum(1 for c in b if c in vowels)
