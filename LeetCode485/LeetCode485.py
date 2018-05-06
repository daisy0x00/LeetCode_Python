# coding:utf-8

class Solution(object):
    def findMaxConsecutiveOnes(self,nums):
        """

        :param nums:  List[int]
        :return:      int
        """
        return max(len(k) for k in (''.join([str(i) for i in nums])).split('0'))


def main():
    nums = [1,1,0,1,1,1,1,0,1,1,1]
    test = Solution()
    print(test.findMaxConsecutiveOnes(nums))

if __name__ == '__main__':
    main()