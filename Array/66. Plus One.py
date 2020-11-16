class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carryin = 1
        for i in range(n-1, -1, -1):
            tmp = digits[i] + carryin
            carryin = tmp // 10
            digits[i] = tmp % 10
        if carryin == 1:
            digits.insert(0, 1)
        return digits
