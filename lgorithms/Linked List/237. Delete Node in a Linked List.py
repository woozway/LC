"""
1. Clarification
2. Possible solutions
    - Swap
3. Coding
4. Tests
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# T=O(1), S=O(1)
class Solution:
    def deleteNode(self, node):
        node.val, node.next = node.next.val, node.next.next
