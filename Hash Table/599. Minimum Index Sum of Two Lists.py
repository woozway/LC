"""
1. Clarification
2. Possible solutions
     - hashmap
3. Coding
4. Tests
"""


# T=O(l1*l2*x), S=O(l1*l2*x), x: avg len of strs
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index1 = {list1[i]: i for i in range(len(list1))}
        index2 = {list2[i]: i for i in range(len(list2))}
        agreements = set(list1) & set(list2)
        sum_index = {s : index1[s] + index2[s] for s in agreements}
        return [s for s in agreements if sum_index[s] == min(sum_index.values())]
