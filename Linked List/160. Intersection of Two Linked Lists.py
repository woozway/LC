"""
1. Clarification
2. Possible solutions
     - Brute force
     - Hash table
     - Two Pointers
3. Coding
4. Tests
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# # T=O(nm), S=O(1), Time Limit Exceeded
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         if not headA or not headB: return None
#         while headA is not None:
#             pB = headB
#             while pB is not None:
#                 if headA == pB:
#                     return headA
#                 pB = pB.next
#             headA = headA.next
#         return None


# T=O(n+m), S=O(m)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB: return None
        nodes_in_B = set()
        while headB is not None:
            nodes_in_B.add(headB)
            headB = headB.next
        while headA is not None:
            if headA in nodes_in_B:
                return headA
            headA = headA.next
        return None


# T=O(n+m), S=O(1)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB: return None
        pA = headA
        pB = headB
        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next
        return pA
