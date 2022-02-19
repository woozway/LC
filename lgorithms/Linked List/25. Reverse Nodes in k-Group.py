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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1, head)
        pre = dummy
        while head:
            tail = pre
            for _ in range(k):
                tail = tail.next
                if tail is None:
                    return dummy.next
            rest = tail.next
            head, tail = self.reverse(head, tail)
            pre.next, head, pre = head, rest, tail
        return dummy.next

    def reverse(self, head, tail):
        pre, cur = tail.next, head
        while pre != tail:
            cur.next, cur, pre = pre, cur.next, cur
        return tail, head
