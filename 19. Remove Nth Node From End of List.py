class Solution:
    """
    two pointers, runner and chaser
    singly-linked list traversal in one pass
    """
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1, head)
        runner = chaser = dummy
        for i in range(n):
            runner = runner.next
        while runner.next:
            runner, chaser = runner.next, chaser.next
        chaser.next = chaser.next.next
        return dummy.next
