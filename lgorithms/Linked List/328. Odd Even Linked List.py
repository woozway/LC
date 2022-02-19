"""
1. Clarification
2. Possible solutions
     - Intuition
     - Merge
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
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head: return head
        odd, even = ListNode(0), ListNode(0)
        prevodd, preveven = odd, even
        cur, cnt = head, 1
        while cur:
            if cnt % 2 == 1:
                prevodd.next = cur
                prevodd = cur
            else:
                preveven.next = cur
                preveven = cur
            cur = cur.next
            cnt += 1
        prevodd.next, preveven.next = None, None
        if odd.next is None:
            odd.next = even.next
        else:
            prevodd.next = even.next
        return odd.next


# T=O(n), S=O(1)
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head: return head
        evenHead = head.next
        odd, even = head, evenHead
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head
