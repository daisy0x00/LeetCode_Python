#coding:utf-8
# 这个代码写的是用暴力穷举法解决LeetCode1两数之和问题

class Solution():
    def twoSum(self, nums, target):
        """

        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return i,j


if __name__ == '__main__':
    nums = [2, 11, 7, 8]
    target = 4
    test = Solution()
    print(test.twoSum(nums, target))