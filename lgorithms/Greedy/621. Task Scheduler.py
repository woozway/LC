"""
1. Clarification
2. Possible solutions
    - Simulation
    - Maths
3. Coding
4. Tests
"""


# T=O(m * len(tasks)), S=O(m)
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)
        m = len(freq)
        nextValid = [1] * m
        rest = list(freq.values())

        time = 0
        for i in range(len(tasks)):
            time += 1
            minNextValid = min(nextValid[j] for j in range(m) if rest[j] > 0)
            time = max(time, minNextValid)
            best = -1
            for j in range(m):
                if rest[j] and nextValid[j] <= time:
                    if best == -1 or rest[j] > rest[best]:
                        best = j
            nextValid[best] = time + n + 1
            rest[best] -= 1
        return time


# T=O(m + len(tasks)), S=O(m)
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)
        maxExec = max(freq.values())
        maxCount = sum(1 for v in freq.values() if v == maxExec)
        return max((maxExec - 1) * (n + 1) + maxCount, len(tasks))
