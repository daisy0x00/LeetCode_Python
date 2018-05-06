# coding:utf-8

class Solution(object):
    def canWinNim(self,n):
        """

        :param n: int
        :return:  bool
        """

        return  n % 4 != 0

def main():
    n = int(input("Please input n:"))
    test = Solution()
    print(test.canWinNim(n))


if __name__ == '__main__':
    main()


