"""
1. Clarification
2. Possible solutions
    - Recursive preorder
3. Coding
4. Tests
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    def serialize(self, root: TreeNode) -> str:
        def rserialize(node):
            if not node:
                strList.append("#,")
                return
            strList.append(str(node.val) + ",")
            rserialize(node.left)
            rserialize(node.right)

        strList = list()
        rserialize(root)
        return "".join(strList)

    def deserialize(self, data: str) -> TreeNode:
        def rdeserialize():
            if dq and dq[0] == "#":
                dq.popleft()
                return None
            root = TreeNode(int(dq.popleft()))
            root.left  = rdeserialize()
            root.right = rdeserialize()
            return root

        strList = data.strip(",").split(",")
        dq = deque(strList)
        return rdeserialize()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
