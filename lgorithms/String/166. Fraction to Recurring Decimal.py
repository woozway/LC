"""
1. Clarification
2. Possible solutions
    - Long division
3. Coding
4. Tests
"""


# T=O(n), S=O(n)
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        fraction = list()
        if (numerator < 0) ^ (denominator < 0):
            fraction.append("-")
        numerator, denominator = abs(numerator), abs(denominator)
        q, r = divmod(numerator, denominator)
        fraction.append(str(q))
        if r == 0:
            return "".join(fraction)
        fraction.append(".")
        hashMap = dict()
        while r:
            if r in hashMap:
                idx = hashMap[r]
                fraction = fraction[:idx] + ["("] + fraction[idx:] + [")"]
                break
            hashMap[r] = len(fraction)
            r *= 10
            q, r = divmod(r, denominator)
            fraction.append(str(q))
        return "".join(fraction)
