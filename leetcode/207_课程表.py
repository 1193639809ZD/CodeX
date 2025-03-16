#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#


# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        adjacency = defaultdict(list)
        queue = deque()
        # 生成入度表和邻接表
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)
        # 将入度为0的点，放入队列中
        for i in range(len(indegrees)):
            if not indegrees[i]:
                queue.append(i)
        # 广度遍历 TopSort.
        while queue:
            pre = queue.popleft()
            numCourses -= 1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]:
                    queue.append(cur)
        return not numCourses


# @lc code=end
