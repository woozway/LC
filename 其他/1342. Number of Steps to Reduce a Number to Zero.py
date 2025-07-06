class Solution:
    def numberOfSteps (self, num: int) -> int:
        tmp = bin(num)[2:]
        return tmp.count('1') * 2 + tmp.count('0') - 1
