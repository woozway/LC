class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {c : i for i, c in enumerate(order)}
        return words == sorted(words, key=lambda w: [d[x] for x in w])
