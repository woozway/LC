class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        """
        inside slice [i, i+m*k) of length m*k
        check to see if every segement [i, i+m) is the same with each other
        """
        n = len(arr)
        if n < m*k:
            return False
        for i in range(0, n-m*k+1):
            flag = 1
            for j in range(i+m, i+m*k):
                if arr[j] != arr[j-m]:
                    flag = 0
            if flag == 1: return True
        return False
