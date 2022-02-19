"""
1. Clarification
2. Possible solutions
    - Histogram
    - Monotonic Stack
3. Coding
4. Tests
"""


# T=O(m^2*n), S=O(m*n)
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        left = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    left[i][j] = (0 if j == 0 else left[i][j - 1]) + 1
        ret = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    continue
                width = left[i][j]
                area = width
                for k in range(i - 1, -1, -1):
                    width = min(width, left[k][j])
                    area = max(area, (i - k + 1) * width)
                ret = max(ret, area)
        return ret


# T=O(m*n), S=O(m*n)
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        left = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    left[i][j] = (0 if j == 0 else left[i][j - 1]) + 1
        ret = 0
        for j in range(n):
            up, down = [0] * m, [0] * m
            stack = []
            for i in range(m):
                while stack and left[stack[-1]][j] >= left[i][j]:
                    stack.pop()
                up[i] = -1 if not stack else stack[-1]
                stack.append(i)
            stack = []
            for i in range(m - 1, -1, -1):
                while stack and left[stack[-1]][j] >= left[i][j]:
                    stack.pop()
                down[i] = m if not stack else stack[-1]
                stack.append(i)
            for i in range(m):
                height = down[i] - up[i] - 1
                area = height * left[i][j]
                ret = max(ret, area)
        return ret
