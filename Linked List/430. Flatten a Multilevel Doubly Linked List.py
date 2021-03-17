"""
1. Clarification
2. Possible solutions
     - Recursive dfs
     - Iterative dfs
3. Coding
4. Tests
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

# T=O(n), S=O(n)
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return head
        pseudoHead = Node(None, None, head, None)
        self.flatten_dfs(pseudoHead, head)
        pseudoHead.next.prev = None
        return pseudoHead.next

    def flatten_dfs(self, prev, curr):
        if not curr: return prev
        curr.prev = prev
        prev.next = curr
        tempNext = curr.next
        tail = self.flatten_dfs(curr, curr.child)
        curr.child = None
        return self.flatten_dfs(tail, tempNext)


# T=O(n), S=O(n)
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return
        pseudoHead = Node(0, None, head, None)
        prev = pseudoHead
        stack = []
        stack.append(head)
        while stack:
            curr = stack.pop()
            prev.next = curr
            curr.prev = prev
            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                curr.child = None
            prev = curr
        pseudoHead.next.prev = None
        return pseudoHead.next
