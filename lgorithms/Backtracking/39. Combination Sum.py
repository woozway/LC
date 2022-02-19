"""
1. Clarification
2. Possible solutions
    - Backtracking
3. Coding
4. Tests
"""


# T=O(sum(feasible solutions' len)), S=O(target)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or target < 1: return []
        ans, tmp = [], []
        def backtrack(idx, Sum):
            if idx >= len(candidates) or Sum >= target:
                if Sum == target:
                    ans.append(tmp[:])
                return
            tmp.append(candidates[idx])
            backtrack(idx, Sum + candidates[idx])
            tmp.pop()
            backtrack(idx + 1, Sum)

        backtrack(0, 0)
        return ans
