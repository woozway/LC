class RandomizedCollection:
    """
    dict[val] = index of val in list v
    when do removing, get any one index of the val to be deleted in v, 
    and denote it as idx, then swap it with the last val in v (if with 
    a different index), change index to idx and then pop it out
    """
    def __init__(self):
        self.v = []
        self.d = {}
        
    def insert(self, val: int) -> bool:
        self.v.append(val)
        if val in self.d:
            self.d[val].add(len(self.v)-1)
            return False
        else:
            self.d[val] = {len(self.v)-1}
            return True
        
    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        last = len(self.v)-1
        idx = self.d[val].pop()
        if not len(self.d[val]):
            del self.d[val]
        if idx != last:
            self.v[idx] = self.v[last]
            self.d[self.v[idx]].remove(last)
            self.d[self.v[idx]].add(idx)
        self.v.pop()
        return True
    
    def getRandom(self) -> int:
        if self.v:
            return self.v[random.randint(0, len(self.v)-1)]
