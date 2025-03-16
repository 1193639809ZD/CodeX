#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#


# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, cur, distance = len(nums), 0, 0
        while cur <= distance:
            distance = max(distance, cur + nums[cur])
            if distance >= n - 1:
                return True
            cur += 1
        return False


# @lc code=end
