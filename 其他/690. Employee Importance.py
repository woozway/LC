"""
1. Clarification
2. Possible solutions
    - dfs
    - bfs
3. Coding
4. Tests
"""


"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

# T=O(n), S=O(n)
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emap = {e.id: e for e in employees}
        def dfs(eid):
            employee = emap[eid]
            return (employee.importance +
                    sum(dfs(eid) for eid in employee.subordinates))
        return dfs(id)


# T=O(n), S=O(n)
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emap = {e.id: e for e in employees}
        total = 0
        Q = collections.deque([id])
        while Q:
            idx = Q.popleft()
            employee = emap[idx]
            total += employee.importance
            for sub in employee.subordinates:
                Q.append(sub)
        return total
