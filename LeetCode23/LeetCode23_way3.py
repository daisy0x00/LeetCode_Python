#coding:utf-8

from queue import PriorityQueue


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
        head = point = ListNode(0)
        q = PriorityQueue()
        ##############修改部分##########
        for index, l in enumerate(lists):
            if l:
                q.put((l.val, index, 0, l))
        ###############################
        while not q.empty():
            ##############修改部分##########
            val, id, index, node = q.get()
            ##############修改部分##########
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                ##############修改部分##########
                q.put((node.val, id, index + 1, node))
                ##############修改部分##########


        return head.next