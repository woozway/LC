"""
1. Clarification
2. Possible solutions
     - Brute force
     - HashMap v1
     - HashMap v2
3. Coding
4. Tests
"""


# T=O(x*(n1+n2)^2), S=O(r*x), x=average len of strings, r=len(ret)
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        if not list1 or not list2: return []
        ret = []
        n1, n2 = len(list1), len(list2)
        for Sum in range(n1 + n2 - 1):
            for i in range(Sum + 1):
                if i < n1 and Sum - i < n2 and list1[i] == list2[Sum - i]:
                    ret.append(list1[i])
            if len(ret) > 0:
                break
        return ret


# T=O(n1*n2*x), S=O(n1*n2*x)
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        if not list1 or not list2: return []
        n1, n2 = len(list1), len(list2)
        hashMap = {}
        for i in range(n1):
            for j in range(n2):
                if list1[i] == list2[j]:
                    if i + j not in hashMap:
                        hashMap[i + j] = []
                    hashMap[i + j].append(list1[i])
        min_index_sum = min(hashMap.keys())
        return hashMap[min_index_sum]


# T=O(n1+n2), S=O(n1*x)
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        if not list1 or not list2: return []
        n1, n2 = len(list1), len(list2)
        hashMap = {x: i for i, x in enumerate(list1)}
        ret = []
        min_sum = inf
        for j, y in enumerate(list2):
            if j > min_sum:
                break
            if y in hashMap:
                Sum = j + hashMap[y]
                if Sum < min_sum:
                    ret.clear()
                    ret.append(y)
                    min_sum = Sum
                elif Sum == min_sum:
                    ret.append(y)
        return ret
