class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minn = inf
        n = len(arr)
        for i in range(1, n):
            minn = min(arr[i]-arr[i-1], minn)
        ans = []
        for i in range(1, n):
            if minn == arr[i] - arr[i-1]:
                ans.append([arr[i-1], arr[i]])
        return ans
