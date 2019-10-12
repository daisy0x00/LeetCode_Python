#coding:utf-8

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def swapPairs(self, head):
        """

        :param head: ListNode
        :return: ListNode
        """
        thead = ListNode(-1)
        thead.next = head
        c = head

        while c.next and c.next.next:
            a, b = c.next, c.next.next
            c.next, a.next = b, b.next
            b.next = a
            c = c.next.next

        return head.next

