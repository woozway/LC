"""
1. Clarification
2. Possible solutions
     - Pythonic built-in
     - Hand-crafted
     - Deque
3. Coding
4. Tests
"""


# # T=O(n), S=O(n)
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         if not s: return ''
#         return ' '.join(reversed(s.split()))


# T=O(n), S=O(n) in python or O(1) in c++
class Solution:
    def reverseWords(self, s: str) -> str:
        if not s: return ''
        l = self.trim_spaces(s)
        self.reverse(l, 0, len(l) - 1)
        self.reverse_each_word(l)
        return ''.join(l)

    def trim_spaces(self, s: str) -> list:
        left, right = 0, len(s) - 1
        while left <= right and s[left] == ' ':
            left += 1
        while left <= right and s[right] == ' ':
            right -= 1
        output = []
        while left <= right:
            if s[left] != ' ':
                output.append(s[left])
            elif output[-1] != ' ':
                output.append(s[left])
            left += 1
        return output

    def reverse(self, l: list, left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1

    def reverse_each_word(self, l: list) -> None:
        n = len(l)
        start = end = 0
        while start < n:
            while end < n and l[end] != ' ':
                end += 1
            self.reverse(l, start, end - 1)
            start = end + 1
            end += 1


# # T=O(n), S=O(n)
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         if not s: return ''
#         left, right = 0, len(s) - 1
#         while left <= right and s[left] == ' ':
#             left += 1
#         while left <= right and s[right] == ' ':
#             right -= 1
#         d, word = collections.deque(), []
#         while left <= right:
#             if s[left] == ' ' and word:
#                 d.appendleft(''.join(word))
#                 word = []
#             elif s[left] != ' ':
#                 word.append(s[left])
#             left += 1
#         d.appendleft(''.join(word))
#         return ' '.join(d)
