"""
1. Clarification
2. Possible solutions
    - Stack
    - Pre-processing
3. Coding
4. Tests
"""


# T=O(n^2), S=O(n)
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == ')':
                lst = []
                while stack and stack[-1] != '(':
                    lst.append(stack.pop())
                stack.pop()
                stack.append(''.join(lst)[::-1])
            else:
                stack.append(ch)
        ans = ''
        while stack:
            ans += stack.pop()
        return ans[::-1]


# T=O(n), S=O(n)
class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        pair = [0] * n
        stack = list()
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                j = stack.pop()
                pair[i], pair[j] = j, i
        ret, index, step = '', 0, 1
        while index < n:
            if s[index] == '(' or s[index] == ')':
                index = pair[index]
                step = -step
            else:
                ret += s[index]
            index += step
        return ret
