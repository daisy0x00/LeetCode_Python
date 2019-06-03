#coding:utf-8

class Solution():
    def removeDuplicates(self, nums):
        """

        :param nums: List[int]
        :return: int
        """
        if len(nums) <= 1:
            return len(nums)

        s = 0
        for f in range(1, len(nums)):
            if nums[s] != nums[f]:
                s += 1
                nums[s] = nums[f]

        return s + 1

def main():
    test = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(test.removeDuplicates(nums))

if __name__ == '__main__':
    main()