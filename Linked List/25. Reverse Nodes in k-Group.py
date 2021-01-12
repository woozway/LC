"""
1. Clarification
2. Possible solutions
 - use dummy head & reverse ListNode in k-slot
3. Coding
4. Tests
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# T=O(n), S=O(1)
class Solution:

    def reverse(self, head, tail):
        cur, prev = head, tail.next
        while prev != tail:
            cur.next, prev, cur = prev, cur, cur.next
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next, pre = head, dummy

        while head:
            tail = pre
            for _ in range(k):
                tail = tail.next
                if tail is None:
                    return dummy.next
            nex = tail.next
            head, tail = self.reverse(head, tail)

            pre.next, tail.next = head, nex
            pre, head = tail, tail.next

        return dummy.next
