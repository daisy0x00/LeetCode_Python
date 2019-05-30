#coding:utf-8

class Solution():
    def missingNumber(self, nums):
        """

        :param nums: List[int]
        :return: int
        """
        res = len(nums)
        for i in range(len(nums)):
            res ^= (i ^ nums[i])

        return res

def main():
    test = Solution()
    nums = [3, 4, 1, 5, 6, 8, 7, 2]
    print(test.missingNumber(nums))

if __name__ == '__main__':
    main()