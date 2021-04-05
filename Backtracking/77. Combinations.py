"""
1. Clarification
2. Possible solutions
    - Python built-in
    - Backtracking or recursive
    - Non-recursive
3. Coding
4. Tests
"""


# T=O((n, k)*k), S=O(k)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n < 1 or k < 1: return [[]]
        return list(itertools.combinations(range(1, n + 1), k))


# T=O((n, k)*k), S=O(n)
class Solution:
    def __init__(self):
        self.tmp = []
        self.ans = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        if n < 1 or k < 1: return [[]]
        self.dfs(1, n, k)
        return self.ans

    def dfs(self, cur, n, k):
        if len(self.tmp) + (n - cur + 1) < k: return
        if len(self.tmp) == k:
            self.ans.append(self.tmp[:])
            return
        self.tmp.append(cur)
        self.dfs(cur + 1, n, k)
        self.tmp.pop()
        self.dfs(cur + 1, n, k)


# T=O((n, k)*k), S=O(k)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n < 1 or k < 1: return [[]]
        tmp, ans = [], []
        for i in range(1, k + 1):
            tmp.append(i)
        tmp.append(n + 1)
        j = 0
        while j < k:
            ans.append(tmp[:k])
            j = 0
            while j < k and tmp[j] + 1 == tmp[j + 1]:
                tmp[j] = j + 1
                j += 1
            tmp[j] += 1
        return ans
