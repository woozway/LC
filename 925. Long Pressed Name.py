class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        flag = True
        pre = '#'
        i, j = 0, 0
        while i < len(name):
            while j<len(typed) and typed[j]!=name[i] and typed[j]==pre: j += 1
            if j<len(typed) and typed[j]==name[i]:
                j += 1
            else:
                flag = False
                break
            pre = name[i]
            i += 1
        while j<len(typed) and typed[j]==pre: j += 1
        return True if flag==True and j>=len(typed) else False