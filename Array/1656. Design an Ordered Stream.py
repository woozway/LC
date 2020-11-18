class OrderedStream:

    def __init__(self, n: int):
        self.val = [None]*n
        self.ptr = 0

    def insert(self, id: int, value: str) -> List[str]:
        self.val[id-1] = value
        ans = []
        while self.ptr < len(self.val) and self.val[self.ptr]:
            ans.append(self.val[self.ptr])
            self.ptr += 1
        return ans
