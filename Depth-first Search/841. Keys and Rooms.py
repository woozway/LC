"""
1. Clarification
2. Possible solutions
     - dfs
     - bfs
3. Coding
4. Tests
"""


# T=O(n+e), S=O(n)
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not rooms: return False
        seen = [False] * len(rooms)
        seen[0] = True
        stack = [0]
        while stack:
            node = stack.pop()
            for nei in rooms[node]:
                if not seen[nei]:
                    seen[nei] = True
                    stack.append(nei)
        return all(seen)


# # T=O(n+e), S=O(n)
# class Solution:
#     def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
#         if not rooms: return False
#         n = len(rooms)
#         num = 0
#         vis = {0}
#         que = collections.deque([0])
#         while que:
#             x = que.popleft()
#             num += 1
#             for it in rooms[x]:
#                 if it not in vis:
#                     vis.add(it)
#                     que.append(it)
#         return num == n
