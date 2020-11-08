class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = len(nums)
        distinct = { x for x in nums }
        sz = len(distinct)
        ordered = sorted(distinct)
        return ordered[-1] if sz < 3 else ordered[-3]
