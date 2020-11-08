class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        """
        T=O(n), S=O(1)
        """
        n = len(A)
        ans = [0]*n
        i, j, p = 0, n-1, n-1
        while i <= j:
            if abs(A[i]) > abs(A[j]):
                ans[p] = A[i]*A[i]
                i += 1
            else:
                ans[p] = A[j]*A[j]
                j -= 1
            p -= 1
        return ans
