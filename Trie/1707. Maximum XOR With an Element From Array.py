"""
1. Clarification
2. Possible solutions
    - Brute force
    - Offline query + Trie
    - Online query + Trie
3. Coding
4. Tests
"""


#
class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums = sorted(list(set(nums)))
        n = len(nums)
        ans = list()
        for x, m in queries:
            print('m=', m)
            index = bisect.bisect_left(nums, m)
            if index == 0 and nums[0] != m:
                ans.append(-1)
            elif index == n:
                maxans = -1
                for j in range(n):
                    maxans = max(maxans, nums[j]^x)
                ans.append(maxans)
            else:
                maxans = -1
                if nums[index] <= m:
                    limit = index+1
                else:
                    limit = index
                for j in range(limit):
                    maxans = max(maxans, nums[j]^x)
                ans.append(maxans)
        return ans


# T=O(nlgn + qlgq + (n+q)*l), S=O(q + n*l), q=len(queries), l=len(bin(num))
class Trie:
    L = 30

    def __init__(self):
        self.left = None
        self.right = None

    def insert(self, val: int):
        node = self
        for i in range(Trie.L, -1, -1):
            bit = (val >> i) & 1
            if bit == 0:
                if not node.left:
                    node.left = Trie()
                node = node.left
            else:
                if not node.right:
                    node.right = Trie()
                node = node.right

    def getMaxXor(self, val: int) -> int:
        ans, node = 0, self
        for i in range(Trie.L, -1, -1):
            bit = (val >> i) & 1
            check = False
            if bit == 0:
                if node.right:
                    node = node.right
                    check = True
                else:
                    node = node.left
            else:
                if node.left:
                    node = node.left
                    check = True
                else:
                    node = node.right
            if check:
                ans |= 1 << i
        return ans


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n, q = len(nums), len(queries)
        nums.sort()
        queries = sorted([(x, m, i) for i, (x, m) in enumerate(queries)], key=lambda query: query[1])
        ans = [0] * q
        t = Trie()
        idx = 0
        for x, m, qid in queries:
            while idx < n and nums[idx] <= m:
                t.insert(nums[idx])
                idx += 1
            if idx == 0:
                ans[qid] = -1
            else:
                ans[qid] = t.getMaxXor(x)
        return ans


# T=O((n+q)*l), S=O(n*l)
class Trie:
    L = 30

    def __init__(self):
        self.left = None
        self.right = None
        self.min_value = float("inf")

    def insert(self, val: int):
        node = self
        node.min_value = min(node.min_value, val)
        for i in range(Trie.L, -1, -1):
            bit = (val >> i) & 1
            if bit == 0:
                if not node.left:
                    node.left = Trie()
                node = node.left
            else:
                if not node.right:
                    node.right = Trie()
                node = node.right
            node.min_value = min(node.min_value, val)

    def getMaxXorWithLimit(self, val: int, limit: int) -> int:
        node = self
        if node.min_value > limit:
            return -1
        ans = 0
        for i in range(Trie.L, -1, -1):
            bit = (val >> i) & 1
            check = False
            if bit == 0:
                if node.right and node.right.min_value <= limit:
                    node = node.right
                    check = True
                else:
                    node = node.left
            else:
                if node.left and node.left.min_value <= limit:
                    node = node.left
                    check = True
                else:
                    node = node.right
            if check:
                ans |= 1 << i
        return ans


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        t = Trie()
        for val in nums:
            t.insert(val)
        q = len(queries)
        ans = [0] * q
        for i, (x, m) in enumerate(queries):
            ans[i] = t.getMaxXorWithLimit(x, m)
        return ans
