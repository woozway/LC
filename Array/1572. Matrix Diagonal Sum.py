class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n= len(mat)
        ans = sum(mat[i][i] + mat[i][n-1-i] for i in range(n))
        return ans if n%2 == 0 else ans-mat[n//2][n//2]
