# coding:utf-8

class Solution:
    def numJewelsInStones(self,J,S):
        """
        :param J:
        :param S:
        :return:
        """

        L = [s in J for s in S]
        return sum(L)

def main():
    J = input()
    S = input()
    test = Solution()
    print(test.numJewelsInStones(J,S))


if __name__ == '__main__' :
    main()
