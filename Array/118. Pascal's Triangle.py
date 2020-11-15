class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[[0]*(i+1) for i in range(numRows)]
        for i in range(0, numRows):
            for j in range(i+1):
                ans[i][j] = 1 if j == 0 or j == i else ans[i-1][j-1] + ans[i-1][j]
        return ans
