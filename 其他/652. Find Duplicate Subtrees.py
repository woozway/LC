"""
1. Clarification
2. Possible solutions
    - dfs
    - HashMap (unique identifier) v1
    - HashMap + Pythonic v2
3. Coding
4. Tests
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# T=O(n^2), S=O(n^2)
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        def dfs(node):
            if not node: return '#'
            serial = '{},{},{}'.format(node.val, dfs(node.left), dfs(node.right))
            count[serial] += 1
            if count[serial] == 2:
                ans.append(node)
            return serial

        count = collections.Counter()
        ans = []
        dfs(root)
        return ans


# T=O(n), S=O(n)
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        def dfs(node):
            if not node: return '#'
            if node in hashMap: return hashMap[node]
            serial = '{},{},{}'.format(node.val, dfs(node.left), dfs(node.right))
            hashMap[node] = serial
            count[serial] += 1
            if count[serial] == 2:
                ans.append(node)
            return serial

        count = collections.Counter()
        hashMap = {}
        ans = []
        dfs(root)
        return ans


# T=O(n), S=O(n)
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        def lookup(node):
            if node:
                uid = trees[node.val, lookup(node.left), lookup(node.right)]
                count[uid] += 1
                if count[uid] == 2:
                    ans.append(node)
                return uid

        trees = collections.defaultdict()
        trees.default_factory = trees.__len__
        count = collections.Counter()
        ans = []
        lookup(root)
        return ans
