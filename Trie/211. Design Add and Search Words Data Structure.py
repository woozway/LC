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
        self.d = {}

    def addWord(self, word: str) -> None:
        t = self.d
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t['end'] = True

    def search(self, word: str) -> bool:
        cut = False
        def dfs(td, s):
            nonlocal cut
            if cut:
                return True
            t = td
            for i, c in enumerate(s):
                if c == '.':
                    return any(dfs(t[j], s[i + 1: ]) for j in t if j != 'end')
                if c not in t:
                    return False
                t = t[c]
            cut = 'end' in t
            return cut
        return dfs(self.d, word)


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
