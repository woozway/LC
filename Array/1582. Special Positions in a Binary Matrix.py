class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        cnt = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    flag = 0
                    for k in range(m):
                        if mat[k][j] == 1 and k != i:
                            flag = 1
                            break
                    if flag == 1:
                        continue
                    for l in range(n):
                        if mat[i][l] == 1 and l != j:
                            flag = 1
                            break
                    if flag == 1:
                        continue
                    else:
                        cnt += 1
        return cnt
