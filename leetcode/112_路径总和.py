#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        # 如果是叶子节点，检查路径和是否等于 targetSum
        if not root.left and not root.right:
            return root.val == targetSum

        # 递归检查左子树和右子树
        new_target = targetSum - root.val
        return self.hasPathSum(root.left, new_target) or self.hasPathSum(root.right, new_target)


# @lc code=end
