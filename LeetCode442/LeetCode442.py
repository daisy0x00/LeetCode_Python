#coding:utf-8

class Solution():
    def findDuplicates(self, nums):
        """

        :param nums: List[int]
        :return: List[int]
        """

        returnlist = []
        for x in nums:
            if nums[abs(x) - 1] < 0:
                returnlist.append(abs(x))
            else:
                nums[abs(x) - 1] *= -1
        return returnlist


if __name__ == '__main__':
    nums = [4,3,2,7,8,2,3,1]
    print(Solution().findDuplicates(nums))