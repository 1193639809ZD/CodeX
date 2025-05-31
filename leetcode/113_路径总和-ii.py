#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node: TreeNode, remaining_sum: int, path: list[int]):
            if not node:
                return

            # 添加当前节点到路径
            path.append(node.val)

            # 如果是叶子节点且路径和等于目标和，添加路径到结果
            if not node.left and not node.right and remaining_sum == node.val:
                result.append(path.copy())

            # 递归处理左子树和右子树
            dfs(node.left, remaining_sum - node.val, path)
            dfs(node.right, remaining_sum - node.val, path)

            # 回溯：移除当前节点
            path.pop()

        result = []
        dfs(root, targetSum, [])
        return result


# @lc code=end
