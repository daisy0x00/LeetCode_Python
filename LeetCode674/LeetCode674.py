#coding:utf-8

class Solution():
    def findLengthOfLCIS(self, nums):
        """

        :param nums: List[int]
        :return: int
        """
        n = len(nums)
        res = 0
        for i in range(n):
            if i == 0:
                count = 1
            else:
                if nums[i] > nums[i - 1]:
                    count += 1
                else:
                    count = 1
            res = max(res, count)
        return res


def main():
    test = Solution()
    nums = [1,3,5,4,7]
    nums1 = [2, 2, 2, 2]
    print(test.findLengthOfLCIS(nums))
    print(test.findLengthOfLCIS(nums1))

if __name__ == '__main__':
    main()