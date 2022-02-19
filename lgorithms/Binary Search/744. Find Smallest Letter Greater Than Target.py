"""
1. Clarification
2. Possible solutions
    - Record letters seen
    - Linear scan
    - Binary search
3. Coding
4. Tests
"""


# T=O(n), S=O(1)
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if len(letters) < 2: return ''
        seen = set(letters)
        for i in range(1, 26):
            cand = chr((ord(target) - ord('a') + i) % 26 + ord('a'))
            if cand in seen:
                return cand


# T=O(n), S=O(1)
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if len(letters) < 2: return ''
        for c in letters:
            if c > target:
                return c
        return letters[0]


# T=O(lgn), S=O(1)
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if len(letters) < 2: return ''
        index = bisect.bisect(letters, target)
        return letters[index % len(letters)]
