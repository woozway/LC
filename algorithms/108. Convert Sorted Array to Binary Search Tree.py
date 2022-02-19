"""
1. Clarification
2. Possible solutions
    - Inorder, choose the left mid as root
    - Inorder, choose the left or right mid as root
3. Coding
4. Tests
"""


# T=O(n), S=O(lgn)
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right: return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(nums) - 1)


# T=O(n), S=O(lgn)
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right: return None
            mid = (left + right + random.randint(0, 1)) // 2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(nums) - 1)
