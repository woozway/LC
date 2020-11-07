class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans = sorted([(l.count(1), row) for row, l in enumerate(mat)])
        return [row for cnt, row in ans[0:k]]
