"""
1. Clarification
2. Possible solutions
    - Brute force v1
    - Brute force v2
3. Coding
4. Tests
"""


# T=O(1), S=O(1)
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = list()
        for h in range(12):
            for m in range(60):
                if bin(h).count("1") + bin(m).count("1") == turnedOn:
                    ans.append(f"{h}:{m:02d}")
        return ans


# T=O(1), S=O(1)
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def countOne(n):
            ret = 0
            while n:
                n &= n - 1
                ret += 1
            return ret

        ans = []
        for i in range(12):
            for j in range(60):
                if countOne(i) + countOne(j) == turnedOn:
                    ans.append(str(i) + ':' + '{:02}'.format(j))
        return ans
