class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = Counter(nums)
        for k in d:
            if d[k] >= 2:
                return True
        return False
