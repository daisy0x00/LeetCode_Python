#coding:utf-8

#
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
        c_dict = {}
        r = head
        index = 0
        while True:
            index += 1
            c_dict[index] = r
            if r.next is not None:
                r = r.next
            else:
                break
        if n == 1:
            if index == 1:
                return None
            else:
                c_dict[index - 1].next = None
                return head
        elif n == index:
            return head.next
        else:
            c_dict[index - n].next = c_dict[index - n + 2]
            return head