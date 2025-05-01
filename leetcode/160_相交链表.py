#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        first, second = headA, headB
        countA = countB = 0
        # 计算A、B链表长度
        while first:
            first = first.next
            countA += 1
        while second:
            second = second.next
            countB += 1
        # first指针指向长链表，并先走abs(countA - countB)步，让first和second可以同时到链表终点
        if countA > countB:
            first, second = headA, headB
        else:
            first, second = headB, headA
        for i in range(abs(countA - countB)):
            first = first.next
        # 节点相同的条件是地址相同
        while first != second:
            first = first.next
            second = second.next
        return first


# @lc code=end
