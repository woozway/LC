class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        f = lambda word: word.count(min(word))
        ws = sorted(map(f, words))
        n = len(words)
        return [n - bisect_right(ws, x) for x in map(f, queries)]
