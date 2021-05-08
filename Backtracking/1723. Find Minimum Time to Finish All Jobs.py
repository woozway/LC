"""
1. Clarification
2. Possible solutions
    - Binary Search + Backtracking + Pruning
    - Binary Serach v2
3. Coding
4. Tests
"""


# T=O(nlgn + lg(sum(jobs)-max(jobs)) * n!), S=O(n)
class Solution:
    def backtrack(self, jobs, workloads, idx, limit):
        if idx >= len(jobs):
            return True
        cur = jobs[idx]
        for i in range(len(workloads)):
            if workloads[i] + cur <= limit:
                workloads[i] += cur
                if self.backtrack(jobs, workloads, idx + 1, limit):
                    return True
                workloads[i] -= cur
            if workloads[i] == 0:
                break
        return False

    def check(self, jobs, k, limit):
        workloads = [0] * k
        return self.backtrack(jobs, workloads, 0, limit)

    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        if k < 0 or not jobs:
            return 0
        jobs.sort()
        l, r = jobs[0], sum(jobs)
        while l < r:
            mid = (l + r) >> 1
            if self.check(jobs, k, mid):
                r = mid
            else:
                l = mid + 1
        return l


# T=O(nlgn), S=O(n)
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        jobs.sort(reverse=True)

        def dfs(i):
            if i == n: return True
            for j in range(k):
                if cap[j] >= jobs[i]:
                    cap[j] -= jobs[i]
                    if dfs(i + 1): return True
                    cap[j] += jobs[i]
                if cap[j] == x: break
            return False

        left, right = max(jobs), sum(jobs)
        while left < right:
            x = (left + right) // 2
            cap = [x] * k
            if dfs(0):
                right = x
            else:
                left = x + 1
        return left
