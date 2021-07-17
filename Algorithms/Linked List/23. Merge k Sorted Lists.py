"""
1. Clarification
2. Possible solutions
    - Brute force
    - Priority Queue
    - Merge with Divide And Conquer
3. Coding
4. Tests
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# T=O(nlgn), S=O(n)
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        self.nodes = []
        head = point = ListNode()
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next


# T=O(nlgk), S=O(k), k=len(lists)
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        h = [(head.val, idx, head) for idx, head in enumerate(lists) if head is not None]
        heapq.heapify(h)
        dummy = ListNode()
        last = dummy
        while h:
            val, idx, node = heapq.heappop(h)
            last.next, last = node, node
            if last.next is not None:
                heapq.heappush(h, (last.next.val, idx, last.next))
        return dummy.next


# T=O(nlgk), S=O(1)
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None

    def merge2Lists(self, l1, l2):
        head = point = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next = l2
        else:
            point.next = l1
        return head.next
