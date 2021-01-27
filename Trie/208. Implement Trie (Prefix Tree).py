"""
1. Clarification
2. Possible solutions
 - Trie (dictionary tree)
3. Coding
4. Tests
"""

# insert: T=O(m), S=O(m)
# search: T=O(m), S=O(1)
# startsWith: T=O(m), S=O(1)
class Trie:

    def __init__(self):
        self.root = {}
        self.end_of_word = '#'

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[self.end_of_word] = self.end_of_word

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_of_word in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
