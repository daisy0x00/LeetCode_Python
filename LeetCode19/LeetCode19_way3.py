#coding:utf-8

# 用快慢指针法解决删除链表中倒数第N个元素的问题
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution():
    def removeNthFromEnd(self, head, n):
        """

        :param head: ListNode
        :param n: int
        :return: ListNode
        """
        # 设置两个指针，均指向头结点
        first = second = head
        # 快指针先移动N步
        for _ in range(n):
            first = first.next
        # 当极端情况下，即first指向了最后一个节点，且要删除的是第一个节点（倒数第N个）
        if not first:
            return head.next
        # 将两个指针同步移动
        # 直到first指向了最后一个节点（两个指针始终保持相同的间隔N-1）
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return head