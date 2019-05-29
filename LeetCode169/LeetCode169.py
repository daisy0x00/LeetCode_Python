#coding:utf-8

from collections import Counter
import math

class Solution():
    def majorityElement(self, nums):
        """

        :param nums: List[int]
        :return: int
        """

        length = math.ceil(len(nums) / 2)

        for k, v in Counter(nums).items():
            if v >= length:
                return k


def main():
    test = Solution()
    #nums = [2,2,1,1,1,2,2]
    #nums = [3, 4, 3, 2, 3, 4]
    nums = [3, 2, 3]
    print(test.majorityElement(nums))

if __name__ == '__main__':
    main()
