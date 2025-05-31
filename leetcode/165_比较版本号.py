#
# @lc app=leetcode.cn id=165 lang=python3
#
# [165] 比较版本号
#


# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # 将版本号按点分割成修订号列表
        v1_parts = version1.split(".")
        v2_parts = version2.split(".")

        # 获取最长的修订号长度
        max_length = max(len(v1_parts), len(v2_parts))

        # 逐个比较修订号
        for i in range(max_length):
            # 获取当前修订号，默认为 0
            v1 = int(v1_parts[i]) if i < len(v1_parts) else 0
            v2 = int(v2_parts[i]) if i < len(v2_parts) else 0

            # 比较修订号
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1

        # 如果所有修订号都相同，返回 0
        return 0


# @lc code=end
