#
# @lc app=leetcode.cn id=841 lang=python3
#
# [841] 钥匙和房间
#


# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # 深度优先遍历，也可以用广度优先遍历
        def dfs(root):
            visited[root] = True

            for node in rooms[root]:
                if visited[node] == False:
                    dfs(node)

        visited = [False] * len(rooms)
        dfs(0)

        for i in range(len(visited)):
            if visited[i] == False:
                return False
        return True

    # def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
    #     # 广度优先遍历
    #     queue = deque()
    #     queue.append(0)
    #     visited = [False] * len(rooms)
    #     visited[0] = True

    #     while queue:
    #         node = queue.popleft()
    #         for next_node in rooms[node]:
    #             if visited[next_node] == False:
    #                 queue.append(next_node)
    #                 visited[next_node] = True

    #     return all(visited)


# @lc code=end
