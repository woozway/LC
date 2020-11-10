class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        """
        T=O(n), S=O(n)
        """
        m = collections.Counter(nums)
        return sum(v * (v - 1) // 2 for k, v in m.items())
