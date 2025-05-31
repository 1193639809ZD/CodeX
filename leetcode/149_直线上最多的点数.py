#
# @lc app=leetcode.cn id=149 lang=python3
#
# [149] 直线上最多的点数
#


# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return n
        max_points = 1  # 至少一个点

        for i in range(n):
            p = points[i]
            slope_count = defaultdict(int)
            duplicates = 0  # 记录与p重合的点的数量（包括p自己）
            current_max = 0

            for j in range(n):
                q = points[j]
                # 判断是否重合
                if p[0] == q[0] and p[1] == q[1]:
                    duplicates += 1
                else:
                    dx = q[0] - p[0]
                    dy = q[1] - p[1]

                    if dx == 0:
                        # 垂直线，用'inf'作为键
                        slope = "inf"
                    else:
                        # 计算最大公约数并约分
                        gcd_val = math.gcd(abs(dx), abs(dy))
                        dx_gcd = dx // gcd_val
                        dy_gcd = dy // gcd_val
                        # 确保分母为正，统一符号
                        if dx_gcd < 0:
                            dx_gcd = -dx_gcd
                            dy_gcd = -dy_gcd
                        slope = (dx_gcd, dy_gcd)

                    slope_count[slope] += 1  # 统计该斜率出现的次数

            # 当前基准点的最大点数为：最多斜率对应的点数 + 重复点数
            if slope_count:
                current_max = max(slope_count.values()) + duplicates
            else:
                # 所有点都是重合点
                current_max = duplicates

            max_points = max(max_points, current_max)

        return max_points


# @lc code=end
