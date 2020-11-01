class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        v = []
        while head:
            v.append(head.val)
            head = head.next
        i, j=0, len(v)-1
        while i<j:
            if v[i]!=v[j]:
                return False;
            i, j = i+1, j-1
        return True
