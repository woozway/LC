"""
1. Clarification
2. Possible solutions
    - Recursion
    - Recursion with Memoization
    - Dynamic programming
3. Coding
4. Tests
"""


# T=O(n), S=O(n)
class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(node):
            if not node:
                return 0, 0
            left = helper(node.left)
            right = helper(node.right)
            rob = node.val + left[1] + right[1]
            not_rob = max(left) + max(right)
            return [rob, not_rob]

        return max(helper(root))


# T=O(n), S=O(n)
class Solution:
    def rob(self, root: TreeNode) -> int:
        rob_saved = {}
        not_rob_saved = {}

        def helper(node, parent_robbed):
            if not node:
                return 0
            if parent_robbed:
                if node in rob_saved:
                    return rob_saved[node]
                result = helper(node.left, False) + helper(node.right, False)
                rob_saved[node] = result
                return result
            else:
                if node in not_rob_saved:
                    return not_rob_saved[node]
                rob = node.val + helper(node.left, True) + helper(node.right, True)
                not_rob = helper(node.left, False) + helper(node.right, False)
                result = max(rob, not_rob)
                not_rob_saved[node] = result
                return result

        return helper(root, False)


# T=O(n), S=O(n)
class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        tree = []
        graph = {-1: []}
        index = -1
        q = [(root, -1)]
        while q:
            node, parent_index = q.pop(0)
            if node:
                index += 1
                tree.append(node.val)
                graph[index] = []
                graph[parent_index].append(index)
                q.append((node.left, index))
                q.append((node.right, index))
        dp_rob = [0] * (index + 1)
        dp_not_rob = [0] * (index + 1)
        for i in reversed(range(index + 1)):
            if not graph[i]:
                dp_rob[i] = tree[i]
                dp_not_rob[i] = 0
            else:
                dp_rob[i] = tree[i] + sum(dp_not_rob[child]
                                          for child in graph[i])
                dp_not_rob[i] = sum(max(dp_rob[child], dp_not_rob[child])
                                    for child in graph[i])
        return max(dp_rob[0], dp_not_rob[0])
