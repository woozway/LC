"""
1. Clarification
2. Possible solutions
    - Trie
    - Queue
3. Coding
4. Tests
"""


# T=O(n), S=O(n)
class WordDictionary:

    def __init__(self):
        self.root = {}
        self.end_of_word = '#'

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[self.end_of_word] = self.end_of_word

    def search(self, word: str) -> bool:
        cut = False
        def dfs(trie, s):
            nonlocal cut
            if cut:
                return True
            t = trie
            for i, c in enumerate(s):
                if c == '.':
                    return any(dfs(t[j], s[i + 1: ]) for j in t if j != self.end_of_word)
                if c not in t:
                    return False
                t = t[c]
            cut = self.end_of_word in t
            return cut
        return dfs(self.root, word)


# T=O(n), S=O(n)
class WordDictionary:

    def __init__(self):
        self.d = collections.defaultdict(list)

    def addWord(self, word: str) -> None:
        self.d[len(word)] += [word]

    def search(self, word: str) -> bool:
        n = len(word)
        f = lambda s: all(map(lambda i: word[i] in {s[i], '.'}, range(n)))
        return any(map(f, self.d[n]))


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
