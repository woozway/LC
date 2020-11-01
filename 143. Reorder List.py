class Solution:
    """
    Do not return anything, modify head in-place instead.
    """
    def reorderList(self, head: ListNode) -> None:
        from collections import deque
        dq = deque()
        tmp = head
        while tmp:
        	dq.append(tmp)
        	tmp = tmp.next
        tmp = ListNode(-1, head)
        while len(dq):
        	if len(dq):
        		tmp.next = dq.popleft()
        		tmp = tmp.next
        	if len(dq):
        		tmp.next = dq.pop()
        		tmp = tmp.next
        tmp.next = None
