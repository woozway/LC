"""
1. Clarification
2. Possible solutions
    - Brute force
    - One pass
3. Coding
4. Tests
"""


# T=O(n^2), S=O(1)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(n):
            curGas = gas[i]
            j, cnt = i, 0
            while cnt < n and curGas >= cost[j]:
                cnt += 1
                curGas -= cost[j]
                j = (j + 1) % n
                curGas += gas[j]
            if cnt == n:
                return i
        return -1


# T=O(n), S=O(1)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n, i = len(gas), 0
        while i < n:
            sumOfGas, sumOfCost, cnt = 0, 0, 0
            while cnt < n:
                j = (i + cnt) % n
                sumOfGas += gas[j]
                sumOfCost += cost[j]
                if sumOfCost > sumOfGas:
                    break
                cnt += 1
            if cnt == n:
                return i
            else:
                i += cnt + 1
        return -1
