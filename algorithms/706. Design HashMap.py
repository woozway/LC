"""
1. Clarification
2. Possible solutions
     - Mod + Array
3. Coding
4. Tests
"""


# T=O(n/k), S=O(k+m), k=len(buckets), m=# of already inserted number
class Bucket:
    def __init__(self):
        self.bucket = []

    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1

    def update(self, key, val):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, val)
                found = True
                break
        if not found:
            self.bucket.append((key, val))

    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]


class MyHashMap:

    def __init__(self):
        self.key_space = 2069
        self.hash_table = [Bucket() for i in range(self.key_space)]

    def put(self, key, val):
        idx = key % self.key_space
        self.hash_table[idx].update(key, val)

    def get(self, key):
        idx = key % self.key_space
        return self.hash_table[idx].get(key)

    def remove(self, key):
        idx = key % self.key_space
        self.hash_table[idx].remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
