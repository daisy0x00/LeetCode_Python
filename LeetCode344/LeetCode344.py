# coding:utf-8

class Solution(object):
    def reverseString(self,s):
        """

        :param s: str
        :return:  str
        """

        return s[::-1]

def main():
    s = input("Please input s:")
    test = Solution()
    print(test.reverseString(s))


if __name__ == '__main__':
    main()