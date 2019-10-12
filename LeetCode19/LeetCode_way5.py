# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        stack,node=[],head
        while(node):
            if node:
                stack.append(node)
                node=node.next
        if stack[-n]==head:return head.next
        prenode=stack[-n-1]
        prenode.next=prenode.next.next
        return head