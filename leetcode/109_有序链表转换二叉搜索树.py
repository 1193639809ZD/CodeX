#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        # 找到链表的中间节点
        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # 断开左右子链表
        if prev:
            prev.next = None

        # 中间节点作为根节点
        root = TreeNode(slow.val)

        # 递归构建左子树和右子树
        root.left = self.sortedListToBST(head if head != slow else None)
        root.right = self.sortedListToBST(slow.next)

        return root


# @lc code=end
