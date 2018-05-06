# coding:utf-8

class Solution(object):
    def selfDividingNumbers(self,left,right):
        """

        :param left:  int
        :param right:  int
        :return:       List[int]
        """

        return list(filter(lambda y:y, map(lambda x:x if all([False if i == '0' else int(x) % int(i) == 0  for i in str(x)]) else False, range(left, right+1))))



def main():
    left = int(input("Please input left:"))
    right = int(input("Please input right:"))

    test = Solution()

    print(test.selfDividingNumbers(left,right))


if __name__ == '__main__' :
    main()