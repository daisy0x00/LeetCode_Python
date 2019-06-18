#coding:utf-8
# 解题思路：先排序，找两端原数组与排序后数组不同的两端，left从最左端开始，right从右端开始到left + 1结束，最后返回right - left + 1

class Solution():
    def findUnsortedSubarray(self, nums):
        """

        :param nums: List[int]
        :return: int
        """
        left = 0
        right = len(nums) - 1
        numsSorted = sorted(nums)

        while left < len(nums) and numsSorted[left] == nums[left]:
            left += 1
        while right > left and numsSorted[right] == nums[right]:
            right -= 1

        return right - left + 1


def main():
    test = Solution()
    nums = [2, 6, 4, 8, 10, 9, 15]
    print(test.findUnsortedSubarray(nums))

if __name__ == '__main__':
    main()