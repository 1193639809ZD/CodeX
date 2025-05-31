#
# @lc app=leetcode.cn id=164 lang=python3
#
# [164] 最大间距
#


# @lc code=start
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        min_val = min(nums)
        max_val = max(nums)

        # 如果所有数字相同，最大间距为 0
        if min_val == max_val:
            return 0

        n = len(nums)
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        num_buckets = (max_val - min_val) // bucket_size + 1

        # 初始化桶
        buckets = [{"min": float("inf"), "max": float("-inf")} for _ in range(num_buckets)]

        # 将元素放入桶中
        for num in nums:
            idx = (num - min_val) // bucket_size
            buckets[idx]["min"] = min(buckets[idx]["min"], num)
            buckets[idx]["max"] = max(buckets[idx]["max"], num)

        # 计算最大间距
        max_gap = 0
        prev_max = min_val

        for bucket in buckets:
            if bucket["min"] == float("inf"):
                continue
            max_gap = max(max_gap, bucket["min"] - prev_max)
            prev_max = bucket["max"]

        return max_gap


# @lc code=end
