"""
1. Clarification
2. Possible solutions
    - Brute force
    - Monotonic stack
3. Coding
4. Tests
"""


# T=O(nm), S=O(m), m=len(next)
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T: return []
        n = len(T)
        ans, nxt, big = [0] * n, dict(), 10**9
        for i in range(n - 1, -1, -1):
            warmer_index = min(nxt.get(t, big) for t in range(T[i] + 1, 102))
            if warmer_index != big:
                ans[i] = warmer_index - i
            nxt[T[i]] = i
        return ans


# T=O(n), S=O(n)
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T: return []
        n = len(T)
        ans = [0] * n
        stack = []
        for i in range(n):
            temperature = T[i]
            while stack and temperature > T[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        return ans
