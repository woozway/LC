"""
1. Clarification
2. Possible solutions
    - Use set to check whether a node has been met before
    - Fast & Slow pointers
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
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next: return False
        S = set()
        while head:
            if head in S:
                return True
            S.add(head)
            head = head.next
        return False


# T=O(n), S=O(1)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next: return False
        slow = fast = head
        while slow and fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                return True
        return False
