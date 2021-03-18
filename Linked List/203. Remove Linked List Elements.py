"""
1. Clarification
2. Possible solutions
     - Make a sentinel
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
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head: return None
        sentinel = ListNode(0, head)
        prev, cur = sentinel, head
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return sentinel.next
