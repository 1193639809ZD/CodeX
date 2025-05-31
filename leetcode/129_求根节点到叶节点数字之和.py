#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根节点到叶节点数字之和
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, current_number: int) -> int:
            if not node:
                return 0

            # 更新当前路径形成的数字
            current_number = current_number * 10 + node.val

            # 如果是叶子节点，返回当前路径形成的数字
            if not node.left and not node.right:
                return current_number

            # 递归处理左子树和右子树
            left_sum = dfs(node.left, current_number)
            right_sum = dfs(node.right, current_number)

            return left_sum + right_sum

        return dfs(root, 0)


# @lc code=end
