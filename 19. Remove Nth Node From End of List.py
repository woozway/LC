# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1, head);
        runner, chaser = dummy, dummy
        for i in range(n): runner = runner.next
        while runner.next: runner, chaser = runner.next, chaser.next
        chaser.next = chaser.next.next
        return dummy.next
    
