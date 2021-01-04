class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        p = dummy
        while p.next:
            if p.next.val != val:
                p = p.next
            else:
                p.next = p.next.next
        return dummy.next
