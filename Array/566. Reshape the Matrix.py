class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(nums)
        n = len(nums[0])
        if m * n != r * c:
            return nums
        ori = [nums[i][j] for i in range(m) for j in range(n)]
        k = 0
        ans = []
        for i in range(r):
            tmp = []
            for j in range(c):
                tmp.append(ori[k])
                k += 1
            ans.append(tmp)
        return ans
