class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        rowsum = [sum(x) for x in mat]
        colsum = [sum(x) for x in zip(*mat)]
        return sum(1 for i in range(m) if rowsum[i]==1 and colsum[mat[i].index(1)]==1)
