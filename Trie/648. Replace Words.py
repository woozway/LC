"""
1. Clarification
2. Possible solutions
    - Prefix Hash
    - Trie
3. Coding
4. Tests
"""


# T=O(sigma(wi^2)), S=O(n), wi=len(i-th word)
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        def replace(word):
            for i in range(1, len(word)):
                if word[:i] in rootset:
                    return word[:i]
            return word

        rootset = set(dictionary)
        return ' '.join(map(replace, sentence.split()))


# T=O(n), S=O(n)
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        def replace(word):
            cur = trie
            for letter in word:
                if letter not in cur or END in cur: break
                cur = cur[letter]
            return cur.get(END, word)

        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True
        for root in dictionary:
            reduce(dict.__getitem__, root, trie)[END] = root
        return ' '.join(map(replace, sentence.split()))
