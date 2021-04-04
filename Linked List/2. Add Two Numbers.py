"""
1. Clarification
2. Possible solutions
    - Elementary Maths
3. Coding
4. Tests
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# T=O(max(m,n)), S=O(max(m,n))
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2: return None
        dummyHead = ListNode(0)
        p, q = l1, l2
        curr = dummyHead
        carry = 0
        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0
            Sum = carry + x + y
            carry = Sum // 10
            curr.next = ListNode(Sum % 10)
            curr = curr.next
            if p: p = p.next
            if q: q = q.next
        if carry:
            curr.next = ListNode(carry)
        return dummyHead.next
