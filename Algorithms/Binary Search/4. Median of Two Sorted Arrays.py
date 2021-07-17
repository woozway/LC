"""
1. Clarification
2. Possible solutions
    - Sort
    - Merge
    - Binary search v1
    - Binary search v2
3. Coding
4. Tests
"""


# T=O((m+n)lg(m+n)), S=O(m+n)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n: nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0: raise ValueError
        ret = sorted(nums1 + nums2)
        mid = (m + n - 1) // 2
        return ret[mid] if (m + n) % 2 else (ret[mid] + ret[mid + 1]) / 2


# T=O(m+n), S=O(m+n)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n: nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0: raise ValueError
        ret = self.merge(nums1, nums2)
        mid = (m + n - 1) // 2
        return ret[mid] if (m + n) % 2 else (ret[mid] + ret[mid + 1]) / 2

    def merge(self, A, B):
        ret = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            if A[i] <= B[j]:
                ret.append(A[i])
                i += 1
            else:
                ret.append(B[j])
                j += 1
        ret.extend(A[i:])
        ret.extend(B[j:])
        return ret


# T=O(lg(m+n)), S=O(1)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
            index1, index2 = 0, 0
            while True:
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])
                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1
                   
        m, n = len(nums1), len(nums2)
        if m > n: nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0: raise ValueError
        totalLength = m + n
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2


# T=O(lg min(m,n)), S=O(1)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n: nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0: raise ValueError
        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and nums2[j-1] > nums1[i]:
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0: max_of_left = nums2[j-1]
                elif j == 0: max_of_left = nums1[i-1]
                else: max_of_left = max(nums1[i-1], nums2[j-1])
                if (m + n) % 2 == 1:
                    return max_of_left
                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])
                return (max_of_left + min_of_right) / 2
