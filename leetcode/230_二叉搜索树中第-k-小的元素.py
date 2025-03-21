#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第 K 小的元素
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 返回中序遍历序列
        def inOrder(root):
            if root:
                inOrder(root.left)
                in_order_list.append(root.val)
                inOrder(root.right)
            else:
                return

        in_order_list = []
        inOrder(root)
        return in_order_list[k - 1]


# @lc code=end
