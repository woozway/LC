class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        T=O(n), S=O(1), in-place,
        need to take care of the boundary case: which is when 
        meeting 0 shoud be duplicate but run out of space in arr
        """
        possible_dups = 0
        right = len(arr) - 1
        for left in range(right + 1):
            if left > right - possible_dups:
                break
            if arr[left] == 0:
                if left == right - possible_dups:
                    arr[right] = 0
                    right -= 1
                    break
                possible_dups += 1
        last = right - possible_dups
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i+possible_dups] = 0
                possible_dups -= 1
                arr[i+possible_dups] = 0
            else:
                arr[i+possible_dups] = arr[i]
