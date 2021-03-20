"""
1. Clarification
2. Possible solutions
     - Hash set
     - Fast & Slow pointers to detect cycle
     - Maths
3. Coding
4. Tests
"""


# T=O(lgn), S=O(lgn)
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        return n == 1


# T=O(lgn), S=O(1), Floyd's cycle detection algo
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum
        
        fast = slow = n
        while slow != 1 and fast != 1 and get_next(fast) != 1:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
            if slow == fast:
                return False
        return True


# # T=O(lgn), S=O(1)
# class Solution:
#     def isHappy(self, n: int) -> bool:
#         def get_next(number):
#             total_sum = 0
#             while number > 0:
#                 number, digit = divmod(number, 10)
#                 total_sum += digit ** 2
#             return total_sum

#         cycle_members = {4, 16, 37, 58, 89, 145, 42, 20}
#         while n != 1 and n not in cycle_members:
#             n = get_next(n)
#         return n == 1
