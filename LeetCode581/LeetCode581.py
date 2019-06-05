#coding:utf-8

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