#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#


# @lc code=start
class Solution:
    def minSubArrayLen_prefix(self, target: int, nums: List[int]) -> int:
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        min_len = float("inf")
        for i in range(1, len(prefix_sum)):
            # 查找满足 prefix_sum[i] - prefix_sum[j] >= target的最右侧的位置
            j = bisect.bisect_right(prefix_sum, prefix_sum[i] - target)
            if j > 0:
                min_len = min(min_len, i - j + 1)

        return min_len if min_len != float("inf") else 0

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """滑动窗口方法

        Args:
            target (int): 目标和
            nums (List[int]): 数组

        Returns:
            int: 起始位置
        """
        left = 0
        window_sum = 0
        min_length = float("inf")

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                min_length = min(min_length, right - left + 1)
                window_sum -= nums[left]
                left += 1

        return min_length if min_length != float("inf") else 0


# @lc code=end
