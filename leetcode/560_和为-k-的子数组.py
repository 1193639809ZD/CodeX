#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#


# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        # 哈希表，前缀和：出现次数
        pre_fix, hash_map = 0, defaultdict(int)
        hash_map[0] = 1

        for num in nums:
            pre_fix += num
            ans += hash_map[pre_fix - k]
            hash_map[pre_fix] += 1

        return ans


# @lc code=end
