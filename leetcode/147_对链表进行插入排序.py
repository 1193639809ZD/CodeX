#
# @lc app=leetcode.cn id=147 lang=python3
#
# [147] 对链表进行插入排序
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # 创建虚拟头节点
        dummy = ListNode(0)
        dummy.next = head
        current = head.next
        prev = head

        while current:
            if current.val < prev.val:
                # 找到插入位置
                insert_pos = dummy
                while insert_pos.next and insert_pos.next.val < current.val:
                    insert_pos = insert_pos.next

                # 插入节点
                prev.next = current.next
                current.next = insert_pos.next
                insert_pos.next = current

                # 更新 current 指针
                current = prev.next
            else:
                # 如果已经有序，继续前进
                prev = current
                current = current.next

        return dummy.next


# @lc code=end
