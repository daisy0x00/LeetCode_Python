#coding:utf-8

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution():
    def mergeKList(self, lists):
        """

        :param lists: ListNode
        :return: ListNode
        """

        self.nodes = []
        head = point = ListNode(0)

        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next

        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next

        return head.next