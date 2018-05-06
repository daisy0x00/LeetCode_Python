# coding:utf-8

class Solution:
    def findComplement(self,num):
        """

        :param num: int
        :return:    int
        """
        l = list(map(lambda x: 0 if int(x) == 1 else 1,bin(num)[2:]))
        l1 =int(''.join([str(i) for i in l]),2)

        return l1


def main():
    num = int(input("Please input num:"))
    test = Solution()
    print(test.findComplement(num))

if __name__ == '__main__':
    main()