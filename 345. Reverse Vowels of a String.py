class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a','e','i','o','u'}
        l = list(s)
        i = 0
        j = len(l)-1
        while i < j:
            if l[i].lower() in vowels and l[j].lower() in vowels:
                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1
            elif l[i].lower() in vowels:
                j -= 1
            elif l[j].lower() in vowels:
                i += 1
            else:
                i += 1
                j -= 1
        return ''.join(l)
