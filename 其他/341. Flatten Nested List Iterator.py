"""
1. Clarification
2. Possible solutions
    - dfs
    - Stack
3. Coding
4. Tests
"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

# T=O(n), S=O(n)
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.lst = []
        self.flattenList(nestedList)

    def flattenList(self, nestedList):
        for x in nestedList:
            if x.isInteger():
                self.lst.append(x.getInteger())
            else:
                self.flattenList(x.getList())

    def next(self) -> int:
        return self.lst.pop(0)

    def hasNext(self) -> bool:
        return 0 < len(self.lst)


# T=O(1), S=O(n)
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.res = []
        self.index = 0
        stack = nestedList
        while stack:
            k = stack[0]
            stack = stack[1:]
            if k.isInteger():
                self.res.append(k)
            else:
                stack = k.getList() + stack

    def next(self) -> int:
        self.index += 1
        return self.res[self.index - 1]

    def hasNext(self) -> bool:
        return self.index < len(self.res)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
