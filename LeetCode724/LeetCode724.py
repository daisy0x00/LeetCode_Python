#coding:utf-8

class Solution():
    def pivotIndex(self, nums):
        """

        :param nums: List[int]
        :return: int
        """
        sumAll = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            if i == 0:
                leftSum = 0
            else:
                leftSum += nums[i - 1]
            if(leftSum * 2 + nums[i] == sumAll):
                return i
        return -1

def main():
    test = Solution()
    nums = [1, 7, 3, 6, 5, 6]
    print(test.pivotIndex(nums))

if __name__ == '__main__':
    main()