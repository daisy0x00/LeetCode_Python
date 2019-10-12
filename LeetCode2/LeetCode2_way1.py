#coding:utf-8

# 解决LeetCode2两数相加问题
# 解题思路是将两个链表转化为数字相加之后，将和转化为链表

class ListNode:
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

        # 先定义一个函数，实现链表转化为数字
        def convert_to_num(self, list):
            num = ''
            while list != None:
                num = str(list.val) + num
                list = list.next

            return int(num)

        # 定义一个函数，实现将数字转化为链表
        def convert_to_link(num):
            root = ListNode(num % 10)
            l3 = root
            num = num // 10
            while num != 0:
                l3.next = ListNode(num % 10)
                l3 = l3.next
                #l3.val = num % 10
                num = num // 10

            return root

        # 用上面定义的函数convert_to_num将两个链表分别转换为num1和num2
        num1, num2 = convert_to_num(l1), convert_to_num(l2)

        # 将两个数字相加得到两数之和
        num = num1 + num2

        # 用函数convert_to_link将两数之和转换为链表
        convert_to_link(num)


if __name__ == '__main__':
    pass


