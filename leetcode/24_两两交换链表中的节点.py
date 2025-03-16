#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
# https://leetcode.cn/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (73.94%)
# Likes:    2380
# Dislikes: 0
# Total Accepted:    1.1M
# Total Submissions: 1.4M
# Testcase Example:  '[1,2,3,4]'
#
# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
#
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]
#
#
# 示例 2：
#
#
# 输入：head = []
# 输出：[]
#
#
# 示例 3：
#
#
# 输入：head = [1]
# 输出：[1]
#
#
#
#
# 提示：
#
#
# 链表中节点的数目在范围 [0, 100] 内
# 0 <= Node.val <= 100
#
#
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 创建一个首节点，保证之后流程一致
        dummyHead = ListNode(0, head)
        temp = dummyHead
        # 保证下面交换的两个节点存在
        while temp.next and temp.next.next:
            node1 = temp.next
            node2 = temp.next.next
            temp.next = node2
            node1.next = node2.next
            node2.next = node1
            temp = node1
        # 返回头节点
        return dummyHead.next


# @lc code=end
