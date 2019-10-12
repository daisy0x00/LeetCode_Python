#coding:utf-8

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def __init__(self):
        self.head = ListNode(0)
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = self.head
        p.next = head
        length = 0
        while p:
            p = p.next
            length += 1

        p = self.head
        target = 0
        while True:
            if target == length - n - 1:
                p.next = p.next.next
                return self.head.next
            p = p.next
            target += 1


