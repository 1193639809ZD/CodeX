#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        # 初始化快慢指针
        slow = head
        fast = head

        # 第一次遍历：检测环的存在
        while fast and fast.next:
            slow = slow.next  # 慢指针每次移动一步
            fast = fast.next.next  # 快指针每次移动两步

            if slow == fast:
                # 存在环，重置一个指针到链表头
                entry = head
                # 第二次遍历：找到环的起始节点
                while entry != slow:
                    entry = entry.next
                    slow = slow.next
                return entry

        # 不存在环
        return None


# @lc code=end
