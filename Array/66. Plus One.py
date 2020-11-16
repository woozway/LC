class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carryin = 1
        for i in range(len(digits)-1, -1, -1):
            tmp = digits[i] + carryin
            carryin = tmp // 10
            digits[i] = tmp % 10
        if carryin:
            digits.insert(0, 1)
        return digits
