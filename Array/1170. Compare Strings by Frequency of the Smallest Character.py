class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        f = lambda word: word.count(min(word))
        ws = sorted(map(f, words))
        n = len(words)
        return [n-bisect.bisect(ws, i) for i in map(f, queries)]
