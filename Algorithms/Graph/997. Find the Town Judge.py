class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        in_degree = [0] * (N + 1)
        out_degree = [0] * (N + 1)
        for a, b in trust:
            in_degree[b] += 1
            out_degree[a] += 1
        for i in range(1, N + 1):
            if in_degree[i] == N - 1 and out_degree[i] == 0:
                return i
        return -1
