class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        S = set(candyType)
        return min(len(candyType)//2, len(S))
