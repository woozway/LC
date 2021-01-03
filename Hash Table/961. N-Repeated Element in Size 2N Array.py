class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        c = collections.Counter(A)
        for k, v in c.items():
            if v == len(A)//2:
                return k
