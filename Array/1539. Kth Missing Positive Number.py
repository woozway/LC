class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """
        T=O(lgn), S=O(1)
        """
        if arr[0] > k:
            return k
        l, r = 0, len(arr)
        while l < r:
            mid = (l + r) >> 1
            x = arr[mid] if mid < len(arr) else inf
            if x - mid - 1 >= k:
                r = mid
            else:
                l = mid + 1
        return k - (arr[l-1] - (l-1) - 1) + arr[l-1]
