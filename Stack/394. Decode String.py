"""
1. Clarification
2. Possible solutions
     - Stack
     - Recursive
3. Coding
4. Tests
"""


# T=O(n), S=O(n)
class Solution:
    def decodeString(self, s: str) -> str:
        if not s or len(s) == 0: return s
        stack = []; curNum = 0; curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + curString * num
            elif c.isdigit():
                curNum = curNum * 10 + int(c)
            else:
                curString += c
        return curString


# # T=O(n), S=O(n)
# class Solution:
#     def decodeString(self, s: str) -> str:
#         if not s or len(s) == 0: return s
#         result, position = self.dfs(0, s, 0, '')
#         return result

#     def dfs(self, position, s, prev_num, prev_str):
#         while position < len(s):
#             while s[position].isdigit():
#                 prev_num  = prev_num * 10 + int(s[position])
#                 position += 1
#             if s[position] == '[':
#                 returned_str, ending_pos = self.dfs(position + 1, s, prev_num=0, prev_str='')
#                 prev_str = prev_str + returned_str*prev_num
#                 position = ending_pos
#                 prev_num = 0
#             elif s[position] == ']':
#                 return prev_str, position
#             else:
#                 prev_str += s[position]
#             position += 1
#         return prev_str, position
