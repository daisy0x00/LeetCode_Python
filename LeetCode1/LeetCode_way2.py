#coding
# 该程序用哈希处理表解决LeetCode1两数之和问题。

class Solution():
    def twoSum(self, nums, target):
        """

        :param nums: List[int]
        :param target: int
        :return: List[int]
        """

        dict = {}

        length = len(nums)
        for x in range(length):
            complement = target - nums[x]
            if complement in dict:
                return [dict[complement], x]
            else:
                dict[nums[x]] = x


if __name__ == '__main__':
    nums = [3, 7, 5, 2, 8, 10]
    target = 9
    test = Solution()
    print(test.twoSum(nums, target))

