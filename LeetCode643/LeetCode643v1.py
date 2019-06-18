#coding:utf-8

class Solution():
    def findMaxAverage(self, nums, k):
        """

        :param nums: List[int]
        :param k: int
        :return: float
        """
        length = len(nums)
        if k == length:
            return sum(nums) * 1.0 / length
        maxSum = sum(nums[:k])
        windowsSum = maxSum
        for i in range(k, length):
            print(i)
            windowsSum += nums[i] - nums[i - k]
            maxSum = max(maxSum, windowsSum)

        return maxSum * 1.0 / k

def main():
    test = Solution()
    nums = [1,12,-5,-6,50,3, 0]
    k = 4
    print(test.findMaxAverage(nums, k))

if __name__ == '__main__':
    main()




