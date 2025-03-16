#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = ListNode(0)
        large = ListNode(0)

        sc, lc = small, large

        while head is not None:
            print(head.val)
            # sleep(1)
            if head.val < x:
                sc.next = head
                sc = sc.next
            else:
                lc.next = head
                lc = lc.next
            head = head.next

        # 切断lc.next指针，否则会形成环路
        sc.next = large.next
        lc.next = None
        return small.next


# @lc code=end
