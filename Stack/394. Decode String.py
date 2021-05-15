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


# T=O(n), S=O(n)
class Solution:
    def decodeString(self, s: str) -> str:
        if not s or len(s) == 0: return s
        ret_str, idx = self.dfs(0, s, 0, '')
        return ret_str

    def dfs(self, idx, s, pre_num, pre_str):
        while idx < len(s):
            while s[idx].isdigit():
                pre_num = pre_num * 10 + int(s[idx])
                idx += 1
            if s[idx] == '[':
                return_str, index = self.dfs(idx + 1, s, 0, '')
                pre_str += return_str * pre_num
                idx = index
                pre_num = 0
            elif s[idx] == ']':
                return pre_str, idx
            else:
                pre_str += s[idx]
            idx += 1
        return pre_str, idx
