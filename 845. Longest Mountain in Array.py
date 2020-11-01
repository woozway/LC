class Solution:
    def longestMountain(self, A: List[int]) -> int:
        n = len(A)
        v1, v2 = [0]*n, [0]*n
        for i in range(n):
            if i == 0: v1[i] = 1
            else: v1[i] = v1[i-1]+1 if A[i]>A[i-1] else 1
        for i in range(n-1, -1, -1):
            if i == n-1: v2[i] = 1
            else: v2[i] = v2[i+1]+1 if A[i]>A[i+1] else 1
        maxn, index = -1, -1
        for i in range(n):
            tot = v1[i]+v2[i]-1
            if maxn < tot:
                index = i
                maxn = tot
            elif maxn==tot and v1[i]>1 and v2[i]>1:
                index = i
        return maxn if index!=-1 and v1[index]>1 and v2[index]>1 and maxn>=3 else 0
