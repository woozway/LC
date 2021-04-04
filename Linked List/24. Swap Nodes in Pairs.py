"""
1. Clarification
2. Possible solutions
    - Swap values in adjacent nodes
    - Only nodes themselves may be changed
    - Recursion
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
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        p = head
        while p and p.next:
            tmp = p.next.next
            p.val, p.next.val = p.next.val, p.val
            p = tmp
        return head


# T=O(n), S=O(1)
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a, b = pre.next, pre.next.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next


# T=O(n), S=O(n)
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        newHead = head.next
        head.next = self.swapPairs(newHead.next)
        newHead.next = head
        return newHead
