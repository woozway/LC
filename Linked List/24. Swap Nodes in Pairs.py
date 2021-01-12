"""
1. Clarification
2. Possible solutions
 - swap values in adjacent nodes
 - only nodes themselves may be changed
3. Coding
4. Tests
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# # T=O(n), S=O(1)
# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         if head is None or head.next is None: return head
#         p = head
#         while p and p.next:
#             tmp = p.next.next
#             p.val, p.next.val = p.next.val, p.val
#             p = tmp
#         return head

# T=O(n), S=O(1)
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a, b = pre.next, pre.next.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next
