#coding:utf-8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroups(self, head, k):
        dummy = ListNode(0)
        p = dummy

        while True:
            count = k
            stack = []
            tmp = head

            while tmp and count:
                stack.append(tmp)
                tmp = tmp.next
                count -= 1

            # 注意，目前tmp所在k+1位置
            # 说明剩下的链表不够k个，跳出循环
            if count:
                p.next = head
                break
            # 翻转操作
            while stack:
                p.next = stack.pop()
                p = p.next
            # 与剩下的链表连接起来
            p.next = tmp
            head = tmp

        return dummy.next