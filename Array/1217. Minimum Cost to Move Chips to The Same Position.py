class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        oddcnt = sum(1 for x in position if x%2 == 1)
        return min(oddcnt, len(position) - oddcnt)
