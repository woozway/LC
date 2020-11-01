class Solution:
    def f(self, s: str) -> list:
        stack = []
        for c in s:
            if c == '#':
                if len(stack): stack.pop()
            else:
                stack.append(c)
        return stack
    
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.f(S) == self.f(T)
