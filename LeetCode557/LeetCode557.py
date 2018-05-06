# coding:utf-8

class Solution(object):
    def reverseWords(self,s):
        """

        :param s: str
        :return:  str
        """
        return (' ').join([word[::-1] for word in s.split(' ')])

def main():
    s = input("Please input s:")
    test = Solution()
    print(test.reverseWords(s))

if __name__ == '__main__':
    main()