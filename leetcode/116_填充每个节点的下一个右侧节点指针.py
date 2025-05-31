#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root or not root.left:
            return root

        # 连接左子节点和右子节点
        root.left.next = root.right

        # 连接右子节点和 next 节点的左子节点
        if root.next:
            root.right.next = root.next.left

        # 递归处理左右子树
        self.connect(root.left)
        self.connect(root.right)

        return root


# @lc code=end
