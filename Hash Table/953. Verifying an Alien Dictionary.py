class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        c2i = {c : i for i, c in enumerate(order)}
        return words == sorted(words, key=lambda w: [c2i[c] for c in w])
