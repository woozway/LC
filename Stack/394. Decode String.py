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
        curNum, curStr = 0, ''
        stackNum, stackStr = [], []
        for c in s:
            if c == '[':
                stackNum.append(curNum)
                stackStr.append(curStr)
                curNum = 0
                curStr = ''
            elif c == ']':
                num = stackNum.pop()
                prevStr = stackStr.pop()
                curStr = prevStr + num * curStr
            elif c.isdigit():
                curNum = curNum * 10 + int(c)
            else:
                curStr += c
        return curStr


# # T=O(n), S=O(n)
# class Solution:
#     def decodeString(self, s: str) -> str:
#         if not s or len(s) == 0: return s
#         result, idx = self.dfs(0, s, 0, '')
#         return result

#     def dfs(self, idx, s, prev_num, prev_str):
#         while idx < len(s):
#             while s[idx].isdigit():
#                 prev_num = prev_num * 10 + int(s[idx])
#                 idx += 1
#             if s[idx] == '[':
#                 returned_str, ending_pos = self.dfs(idx + 1, s, 0, '')
#                 prev_str = prev_str + returned_str*prev_num
#                 idx = ending_pos
#                 prev_num = 0
#             elif s[idx] == ']':
#                 return prev_str, idx
#             else:
#                 prev_str += s[idx]
#             idx += 1
#         return prev_str, idx
