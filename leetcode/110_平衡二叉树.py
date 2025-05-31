#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkBalance(node: TreeNode):
            if not node:
                return True, 0

            # 递归检查左子树
            left_balanced, left_height = checkBalance(node.left)
            if not left_balanced:
                return False, 0

            # 递归检查右子树
            right_balanced, right_height = checkBalance(node.right)
            if not right_balanced:
                return False, 0

            # 检查当前节点是否平衡
            balanced = abs(left_height - right_height) <= 1
            height = max(left_height, right_height) + 1

            return balanced, height

        balanced, _ = checkBalance(root)
        return balanced


# @lc code=end
