#coding:utf-8

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def addTwoNumbers(self, l1, l2):
        """

        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        """
        root= ListNode(0)
        curr = root
        p, q = l1, l2
        carry = 0

        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0
            sum = x + y + carry
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next

        if carry > 0 :
            curr.next = ListNode(carry)
            curr = curr.next

        return root.next
