#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#


# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 辅助比较函数
        def compare(x, y):
            if x + y < y + x:
                return -1
            elif x + y > y + x:
                return 1
            else:
                return 0

        # 将所有数字转换为字符串
        nums_str = [str(num) for num in nums]

        # 自定义排序，从大到小
        nums_str.sort(key=cmp_to_key(compare), reverse=True)

        # 处理前导零的情况
        if nums_str[0] == "0":
            return "0"

        # 连接排序后的字符串
        return "".join(nums_str)


# @lc code=end
