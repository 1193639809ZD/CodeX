#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#


# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0
        current_tank = 0
        start_station = 0

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            current_tank += gas[i] - cost[i]

            # 如果current_tank小于0，就是说这段路程油小于消耗，但是中间没停，表示从起点到中间都是油大于消耗
            # 如果从中间任何一个点开始，表示去掉了更多的油，更少的消耗，最终油依然小于消耗，所以中间都不能做起始点
            # 因此更新起始点为下一个站点
            if current_tank < 0:  # 如果当前油箱中的汽油量小于 0，更新起始加油站
                start_station = i + 1
                current_tank = 0

        return start_station if total_tank >= 0 else -1


# @lc code=end
