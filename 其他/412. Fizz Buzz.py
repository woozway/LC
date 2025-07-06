"""
1. Clarification
2. Possible solutions
    - Naive Approach
    - String Concatenation
    - Hash
3. Coding
4. Tests
"""


# T=O(n), S=O(1)
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for num in range(1, n + 1):
            divisible_by_3 = (num % 3 == 0)
            divisible_by_5 = (num % 5 == 0)
            if divisible_by_3 and divisible_by_5:
                ans.append("FizzBuzz")
            elif divisible_by_3:
                ans.append("Fizz")
            elif divisible_by_5:
                ans.append("Buzz")
            else:
                ans.append(str(num))
        return ans


# T=O(n), S=O(1)
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for num in range(1, n + 1):
            divisible_by_3 = (num % 3 == 0)
            divisible_by_5 = (num % 5 == 0)
            num_ans_str = ""
            if divisible_by_3:
                num_ans_str += "Fizz"
            if divisible_by_5:
                num_ans_str += "Buzz"
            if not num_ans_str:
                num_ans_str = str(num)
            ans.append(num_ans_str)
        return ans


# T=O(n), S=O(1)
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        fizz_buzz_dict = {3: "Fizz", 5: "Buzz"}
        for num in range(1, n + 1):
            num_ans_str = ""
            for key in fizz_buzz_dict.keys():
                if num % key == 0:
                    num_ans_str += fizz_buzz_dict[key]
            if not num_ans_str:
                num_ans_str = str(num)
            ans.append(num_ans_str)
        return ans
