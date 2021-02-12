"""
1. Clarification
2. Possible solutions
 - bfs
 - use those next pointers already established
3. Coding
4. Tests
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# T=O(n), S=O(n)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        Q = collections.deque([root])
        while Q:
            size = len(Q)
            for i in range(size):
                node = Q.popleft()
                if i < size - 1:
                    node.next = Q[0]
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        return root


# # T=O(n), S=O(1)
# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         if not root: return root
#         leftmost = root
#         while leftmost.left:
#             head = leftmost
#             while head:
#                 head.left.next = head.right
#                 if head.next:
#                     head.right.next = head.next.left
#                 head = head.next
#             leftmost = leftmost.left
#         return root
