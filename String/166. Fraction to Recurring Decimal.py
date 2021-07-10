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
        fraction = ""
        if (numerator < 0) ^ (denominator < 0):
            fraction += "-"
        numerator, denominator = abs(numerator), abs(denominator)
        fraction += str(numerator // denominator)
        remainder = numerator % denominator
        if remainder == 0:
            return fraction
        fraction += "."
        hashMap = dict()
        while remainder:
            if remainder in hashMap:
                index = hashMap[remainder]
                fraction = fraction[:index] + "(" + fraction[index:] + ")"
                break
            hashMap[remainder] = len(fraction)
            remainder *= 10
            fraction += str(remainder // denominator)
            remainder %= denominator
        return fraction
