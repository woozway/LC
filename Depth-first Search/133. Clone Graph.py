"""
1. Clarification
2. Possible solutions
     - dfs
     - bfs
3. Coding
4. Tests
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# T=O(n), S=O(n)
class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        if node in self.visited: return self.visited[node]
        clone_node = Node(node.val)
        self.visited[node] = clone_node
        clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        return clone_node


# # T=O(n), S=O(n)
# class Solution:
#     def cloneGraph(self, node: 'Node') -> 'Node':
#         if not node: return None
#         visited = {}
#         Q = collections.deque([node])
#         visited[node] = Node(node.val)
#         while Q:
#             n = Q.popleft()
#             for nei in n.neighbors:
#                 if nei not in visited:
#                     Q.append(nei)
#                     visited[nei] = Node(nei.val)
#                 visited[n].neighbors.append(visited[nei])
#         return visited[node]
