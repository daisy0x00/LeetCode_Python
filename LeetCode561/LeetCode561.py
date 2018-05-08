# coding: utf-8

class Solution(object):
    def arrayPairSum(self,nums):
        """

        :param nums: List[int]
        :return:     int
        """
        return sum(sorted(nums)[::2])


def main():
    nums = [1,4,2,3,8,5,7,6]
    test = Solution()
    print(test.arrayPairSum(nums))

if __name__ == '__main__':
    main()