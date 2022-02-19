"""
1. Clarification
2. Possible solutions
    - stack, greedy, simulation
3. Coding
4. Tests
"""


# T=O(n), S=O(n)
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j = 0
        stack = []
        for x in pushed:
            stack.append(x)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return j == len(popped)
      
