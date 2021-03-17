"""
1. Clarification
2. Possible solutions
     - Use set to check whether a node has been met before
     - Fast & Slow pointers: a = c + (n-1)*(b+c)
3. Coding
4. Tests
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# T=O(n), S=O(n)
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next: return None
        S = set()
        while head:
            if head in S:
                return head
            S.add(head)
            head = head.next
        return None


# T=O(n), S=O(1)
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next: return None
        slow = fast = head
        while slow and fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if fast is slow:
                ptr = head
                while ptr != slow:
                    ptr, slow = ptr.next, slow.next
                return ptr
        return None
