class Solution(object):
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = collections.Counter(deck)
        n = len(deck)
        for x in range(2, n+1):
            if n % x == 0:
                if all(v % x == 0 for v in count.values()):
                    return True
        return False
