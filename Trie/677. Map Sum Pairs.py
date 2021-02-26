"""
1. Clarification
2. Possible solutions
     - brute force
     - Prefix Hashmap
     - trie
3. Coding
4. Tests
"""


# # insert: T=O(1), sum: T=O(np), p=len(input prefix)
# class MapSum:
# 
#     def __init__(self):
#         self.map = {}
# 
#     def insert(self, key, val):
#         self.map[key] = val
# 
#     def sum(self, prefix):
#         return sum(val for key, val in self.map.items()
#                    if key.startswith(prefix))


# # insert: T=O(k^2), sum: T=O(1), k=len(key)
# class MapSum:
# 
#     def __init__(self):
#         self.map = {}
#         self.score = collections.Counter()
# 
#     def insert(self, key, val):
#         delta = val - self.map.get(key, 0)
#         self.map[key] = val
#         for i in range(len(key) + 1):
#             prefix = key[:i]
#             self.score[prefix] += delta
# 
#     def sum(self, prefix):
#         return self.score[prefix]


# insert: T=O(k^2), sum: T=O(1), k=len(key)
class TrieNode:
    __slots__ = 'children', 'score'
    def __init__(self):
        self.children = {}
        self.score = 0


class MapSum:

    def __init__(self):
        self.map = {}
        self.root = TrieNode()

    def insert(self, key, val):
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        cur = self.root
        cur.score += delta
        for char in key:
            cur = cur.children.setdefault(char, TrieNode())
            cur.score += delta

    def sum(self, prefix):
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return 0
            cur = cur.children[char]
        return cur.score


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
