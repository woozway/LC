class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        dic = {}
        for i, c in enumerate(S):
            dic[c] = i
        right = dic[S[0]]
        left = 0
        res = []
        for i, c in enumerate(S):
            right = max(right, dic[c])
            if i >= right:
                res.append(right - left + 1)
                left = right + 1 
        return res
