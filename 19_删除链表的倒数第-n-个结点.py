#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#
# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (50.56%)
# Likes:    3062
# Dislikes: 0
# Total Accepted:    1.7M
# Total Submissions: 3.3M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
#
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
#
#
# 示例 2：
#
#
# 输入：head = [1], n = 1
# 输出：[]
#
#
# 示例 3：
#
#
# 输入：head = [1,2], n = 1
# 输出：[1]
#
#
#
#
# 提示：
#
#
# 链表中结点的数目为 sz
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
#
#
#
#
# 进阶：你能尝试使用一趟扫描实现吗？
#
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def getLength(head: ListNode) -> int:
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        dummy = ListNode(0, head)
        length = getLength(head)
        cur = dummy
        for i in range(1, length - n + 1):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next

    # 快慢指针
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    #     # 创建一个首节点，保证删除流程一致
    #     dummy = ListNode(0, head)
    #     # 声明fast、slow指针，fast先走n步
    #     slow, fast = dummy, head
    #     for _ in range(n):
    #         fast = fast.next
    #     # fast和slow一起走，当fast走到最后一个节点的时候，slow下一个节点即是要删除的节点
    #     while fast:
    #         slow, fast = slow.next, fast.next
    #     slow.next = slow.next.next
    #     return dummy.next


# @lc code=end
