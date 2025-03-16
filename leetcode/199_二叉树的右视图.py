#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 层序遍历
        if not root:
            return []
        ans, queue = [], deque()
        queue.append(root)
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if i == n - 1:
                    ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans


# @lc code=end
