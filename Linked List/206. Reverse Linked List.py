"""
1. Clarification
2. Possible solutions
 - iteratively
 - recursively
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
#     def reverseList(self, head: ListNode) -> ListNode:
#         cur, prev = head, None
#         while cur:
#             cur.next, prev, cur = prev, cur, cur.next
#         return prev

# T=O(n), S=O(n)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: return head
        p = self.reverseList(head.next)
        head.next.next, head.next = head, None
        return p
