#coding:utf-8

# 这个方法是时间复杂度为O(n^2)的穷举法，虽然可以解答，但是超出了时间限制


class Solution():
    def maxSubArray(self, nums):
        """

        :param nums: List[int]
        :return: int
        """

        if len(nums) == 0:
            return 0
        currentSum = maxSum = nums[0]
        for i in range(1, len(nums)):
            currentSum = max(currentSum + nums[i], nums[i])
            maxSum = max(maxSum, currentSum)
        return maxSum

def main():
    test = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    nums1 = [-1]
    print(test.maxSubArray(nums))
    print(test.maxSubArray(nums1))


if __name__ == '__main__':
    main()
