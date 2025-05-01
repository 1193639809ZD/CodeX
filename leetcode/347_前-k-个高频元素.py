#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#


# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ass_dict = defaultdict(int)

        for num in nums:
            ass_dict[num] += 1

        count = sorted(ass_dict, key=lambda x: ass_dict[x], reverse=True)
        return count[:k]


# @lc code=end
