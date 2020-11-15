class Solution:
    def average(self, salary: List[int]) -> float:
        maxValue = max(salary)
        minValue = min(salary)
        return (sum(salary)-maxValue-minValue) / (len(salary)-2)
