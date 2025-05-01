#
# @lc app=leetcode.cn id=1306 lang=python3
#
# [1306] 跳跃游戏 III
#


# @lc code=start
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # 如果当前位置的值为0，符合条件，直接返回True
        if arr[start] == 0:
            return True

        n = len(arr)
        # 访问过的点
        visited = {start}
        queue = deque([start])

        while len(queue) > 0:
            u = queue.popleft()
            # 每个下标是一个节点，可跳跃的下标就是相邻的点
            for v in [u + arr[u], u - arr[u]]:
                # 保证下标在数组范围内，并且没有被访问过
                if 0 <= v < n and v not in visited:
                    if arr[v] == 0:
                        return True
                    queue.append(v)
                    visited.add(v)

        return False


# @lc code=end
