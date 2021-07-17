class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        c = collections.Counter(students)
        for e in sandwiches:
            if c[e] == 0: break
            c[e] -= 1
        return c[0] + c[1]
