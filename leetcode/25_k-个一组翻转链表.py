#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#
# https://leetcode.cn/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (69.11%)
# Likes:    2508
# Dislikes: 0
# Total Accepted:    752.4K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
#
# k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
#
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[2,1,4,3,5]
#
#
# 示例 2：
#
#
#
#
# 输入：head = [1,2,3,4,5], k = 3
# 输出：[3,2,1,4,5]
#
#
#
# 提示：
#
#
# 链表中的节点数目为 n
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000
#
#
#
#
# 进阶：你可以设计一个只用 O(1) 额外内存空间的算法解决此问题吗？
#
#
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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 反转链表，并返回头、尾节点
        def reverseList(reverse_head: Optional[ListNode]):
            dummy = ListNode(0)
            tail = reverse_head
            while reverse_head:
                temp_node = reverse_head
                reverse_head = reverse_head.next
                temp_node.next = dummy.next
                dummy.next = temp_node
            return dummy.next, tail

        # 剩余链表长度是否足够
        def flag(interval_head, k):
            count = 0
            while interval_head:
                count += 1
                interval_head = interval_head.next
                if count == k:
                    return True
            return False

        dummy = ListNode(0, head)
        # 每段链表范围为(start.next, ptr)，注意反转前断开链表，反转后再连接
        start, ptr, end = dummy, dummy, head
        while True:
            if flag(start.next, k):
                for i in range(k):
                    ptr = ptr.next
                    end = end.next
                ptr.next = None
                start.next, ptr = reverseList(start.next)
                # 更新指针
                start = ptr
                ptr.next = end
            else:
                break

        return dummy.next


# @lc code=end
