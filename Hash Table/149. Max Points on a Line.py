"""
1. Clarification
2. Possible solutions
    - Hashing
3. Coding
4. Tests
"""


# T=O(n^2 * lgm), S=O(n)
from collections import Counter
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b);

        n = len(points)
        if n <= 2:
            return n
        ret = 0
        for i in range(n):
            if ret >= n - i or ret > n // 2:
                break
            mp = Counter()
            for j in range(i + 1, n):
                x = points[i][0] - points[j][0]
                y = points[i][1] - points[j][1]
                if x == 0:
                    y = 1
                elif y == 0:
                    x = 1
                else:
                    if y < 0:
                        x, y = -x, -y
                    gcdXY = gcd(abs(x), abs(y))
                    x //= gcdXY
                    y //= gcdXY
                mp[y + x * 20001] += 1
            maxn = 0
            for _, v in mp.items():
                maxn = max(maxn, v + 1)
            ret = max(ret, maxn)
        return ret
