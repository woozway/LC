"""
1. Clarification
2. Possible solutions
    - dfs + memoization
    - Topological sort
3. Coding
4. Tests
"""


# T=O(m*n), S=O(m*n)
from functools import lru_cache

class Solution:

    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        @lru_cache(None)
        def dfs(row: int, col: int) -> int:
            best = 1
            for dx, dy in Solution.DIRS:
                newRow, newCol = row + dx, col + dy
                if 0 <= newRow < rows and 0 <= newCol < cols and matrix[newRow][newCol] > matrix[row][col]:
                    best = max(best, dfs(newRow, newCol) + 1)
            return best

        ans = 0
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                ans = max(ans, dfs(i, j))
        return ans


# T=O(m*n), S=O(m*n)
class Solution:
    
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        outdegrees = [[0] * cols for _ in range(rows)]
        queue = collections.deque()
        for i in range(rows):
            for j in range(cols):
                for dx, dy in Solution.DIRS:
                    newRow, newCol = i + dx, j + dy
                    if 0 <= newRow < rows and 0 <= newCol < cols and matrix[newRow][newCol] > matrix[i][j]:
                        outdegrees[i][j] += 1
                if outdegrees[i][j] == 0:
                    queue.append((i, j))

        ans = 0
        while queue:
            ans += 1
            size = len(queue)
            for _ in range(size):
                row, col = queue.popleft()
                for dx, dy in Solution.DIRS:
                    newRow, newCol = row + dx, col + dy
                    if 0 <= newRow < rows and 0 <= newCol < cols and matrix[newRow][newCol] < matrix[row][col]:
                        outdegrees[newRow][newCol] -= 1
                        if outdegrees[newRow][newCol] == 0:
                            queue.append((newRow, newCol))

        return ans
