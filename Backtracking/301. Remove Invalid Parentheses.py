"""
1. Clarification
2. Possible solutions
    - Backtracking v1
    - Backtracking v2
3. Coding
4. Tests
"""


# T=O(2^n), S=O(n)
class Solution:
    def __init__(self):
        self.valid_expressions = None
        self.min_removed = None

    def reset(self):
        self.valid_expressions = set()
        self.min_removed = math.inf

    def remaining(self, string, index, left_count, right_count, expr, rem_count):
        if index == len(string):
            if left_count == right_count:
                if rem_count <= self.min_removed:
                    possible_ans = ''.join(expr)
                    if rem_count < self.min_removed:
                        self.valid_expressions = set()
                        self.min_removed = rem_count
                    self.valid_expressions.add(possible_ans)
        else:
            current_char = string[index]
            if current_char != '(' and current_char != ')':
                expr.append(current_char)
                self.remaining(string, index + 1, left_count, right_count, expr, rem_count)
                expr.pop()
            else:
                self.remaining(string, index + 1, left_count, right_count, expr, rem_count + 1)
                expr.append(current_char)
                if string[index] == '(':
                    self.remaining(string, index + 1, left_count + 1, right_count, expr, rem_count)
                elif right_count < left_count:
                    self.remaining(string, index + 1, left_count, right_count + 1, expr, rem_count)
                expr.pop()

    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.reset()
        self.remaining(s, 0, 0, 0, [], 0)
        return list(self.valid_expressions)


# T=O(2^n), S=O(n)
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left, right = 0, 0
        for char in s:
            if char == '(':
                left += 1
            elif char == ')':
                right = right + 1 if left == 0 else right
                left = left - 1 if left > 0 else left
        result = {}

        def recurse(s, index, left_count, right_count, left_rem, right_rem, expr):
            if index == len(s):
                if left_rem == 0 and right_rem == 0:
                    ans = ''.join(expr)
                    result[ans] = 1
            else:
                if (s[index] == '(' and left_rem > 0) or (s[index] == ')' and right_rem > 0):
                    recurse(s, index + 1,
                            left_count,
                            right_count,
                            left_rem - (s[index] == '('),
                            right_rem - (s[index] == ')'), expr)
                expr.append(s[index])
                if s[index] != '(' and s[index] != ')':
                    recurse(s, index + 1,
                            left_count,
                            right_count,
                            left_rem,
                            right_rem, expr)
                elif s[index] == '(':
                    recurse(s, index + 1,
                            left_count + 1,
                            right_count,
                            left_rem,
                            right_rem, expr)
                elif s[index] == ')' and left_count > right_count:
                    recurse(s, index + 1,
                            left_count,
                            right_count + 1,
                            left_rem,
                            right_rem, expr)
                expr.pop()

        recurse(s, 0, 0, 0, left, right, [])
        return list(result.keys())
