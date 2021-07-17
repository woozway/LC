class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ans = []
        textlist = text.split()
        n = len(textlist)
        for i in range(n):
            if first == textlist[i] and i + 1 < n and second == textlist[i+1]:
                if i + 2 < n:
                    ans.append(textlist[i + 2])
        return ans
