#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
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
    def connect(self, root: "Node") -> "Node":
        if not root:
            return root

        # 从根节点开始
        current = root

        while current:
            # 虚拟头节点用于下一层的链接
            dummy = Node()
            pre = dummy

            # 遍历当前层的所有节点
            while current:
                if current.left:
                    pre.next = current.left
                    pre = pre.next
                if current.right:
                    pre.next = current.right
                    pre = pre.next
                # 移动到当前层的下一个节点
                current = current.next

            # 移动到下一层的第一个节点
            current = dummy.next

        return root


# @lc code=end
