# coding:utf-8

class Solution:
    def hasAlternatingBits(self,n):
        """

        :param n: int
        :return:  bool
        """

        return all([i if i== '1' else False for i in bin(n)[2:len(bin(n)):2]]) and all([j if j == '0' else False for j in bin(n)[3:len(bin(n)):2]])

def main():
    n = int(input("Please input n:"))
    test = Solution()
    print(test.hasAlternatingBits(n))

if __name__ == '__main__':
    main()