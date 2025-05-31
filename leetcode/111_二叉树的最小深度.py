#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """层序遍历：碰见第一个叶子节点即使最小深度，比深度优先遍历遍历完树快

        Args:
            root (Optional[TreeNode]): 根节点

        Returns:
            int: 深度
        """
        if not root:
            return 0

        queue = deque([(root, 1)])

        while queue:
            node, depth = queue.popleft()

            # 检查是否为叶子节点
            if not node.left and not node.right:
                return depth

            # 如果有左子节点，加入队列
            if node.left:
                queue.append((node.left, depth + 1))

            # 如果有右子节点，加入队列
            if node.right:
                queue.append((node.right, depth + 1))


# @lc code=end
