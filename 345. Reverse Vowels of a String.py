class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        l = list(s)
        i = 0
        j = len(l)-1
        while i < j:
            if l[i] in vowels and l[j] in vowels:
                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1
            elif l[i] in vowels:
                j -= 1
            elif l[j] in vowels:
                i += 1
            else:
                i += 1
                j -= 1
        return ''.join(l)
