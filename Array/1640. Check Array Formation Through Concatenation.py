class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        for i in pieces:
            if i[0] not in arr or i != arr[arr.index(i[0]):arr.index(i[0])+len(i)]:
                return False
        return True
