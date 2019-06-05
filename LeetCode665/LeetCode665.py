#coding:utf-8

class Solution():
    def checkPossibility(self, nums):
        """

        :param nums: List[int]
        :return: bool
        """

        #    if i - 1 >= 0 and nums[i - 1] > nums[i + 1] and i + 2 < len(nums) and nums[i] > nums[i + 2]:
        res = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                res += 1
            if i - 1 >= 0 and nums[i - 1] > nums[i + 1] and i + 2 < len(nums) and nums[i] > nums[i + 2]:
                return False
        return res <= 1


def main():
    test = Solution()
    nums = [4,2,1]
    nums1 = [4,2,3]
    print(test.checkPossibility(nums))
    print(test.checkPossibility(nums1))

if __name__ == '__main__':
    main()
