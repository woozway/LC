"""
1. Clarification
2. Possible solutions
    - Hashing v1, gcd
    - Hashing v2
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


# T=O(n^2), S=O(n)
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def max_points_on_a_line_containing_point_i(i):
            def slope_coprime(x1, y1, x2, y2):
                delta_x, delta_y = x1 - x2, y1 - y2
                if delta_x == 0:
                    return 0, 0
                elif delta_y == 0:
                    return sys.maxsize, sys.maxsize
                elif delta_x < 0:
                    delta_x, delta_y = - delta_x, - delta_y
                gcd = math.gcd(delta_x, delta_y)
                slope = (delta_x / gcd, delta_y / gcd)
                return slope

            def add_line(i, j, count, duplicates):
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]
                if x1 == x2 and y1 == y2:
                    duplicates += 1
                elif y1 == y2:
                    nonlocal horizontal_lines
                    horizontal_lines += 1
                    count = max(horizontal_lines, count)
                else:
                    slope = slope_coprime(x1, y1, x2, y2)
                    lines[slope] = lines.get(slope, 1) + 1
                    count = max(lines[slope], count)
                return count, duplicates

            lines, horizontal_lines = {}, 1
            count = 1
            duplicates = 0
            for j in range(i + 1, n):
                count, duplicates = add_line(i, j, count, duplicates)
            return count + duplicates

        n = len(points)
        if n < 3:
            return n

        max_count = 1
        for i in range(n - 1):
            max_count = max(max_points_on_a_line_containing_point_i(i), max_count)
        return max_count
