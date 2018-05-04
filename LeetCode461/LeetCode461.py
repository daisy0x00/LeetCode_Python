# coding:utf-8

import re

class Solution:
    def hammingDistance(self,x,y):
        """

        :param x: int
        :param y: int
        :return:  int
        """
        return len(re.findall('1',str(bin(x ^ y))))


def main():
    x = int(input("Please input x:"))
    y = int(input("Please input y:"))

    test = Solution()
    print(test.hammingDistance(x,y))

if __name__ == '__main__':
    main()