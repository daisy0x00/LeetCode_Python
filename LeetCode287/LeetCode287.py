# coding:utf-8

class Solution():
    def findDuplicate(self, nums):
        """

        :param nums: List[int]
        :return: int
        """
        if len(nums) > 1:
            slow = nums[0]
            fast = nums[nums[0]]
            while slow != fast:
                slow = nums[slow]
                fast = nums[nums[fast]]

            entry = 0
            while entry != slow:
                entry = nums[entry]
                slow = nums[slow]

            return entry
        return -1

if __name__ == '__main__':
    nums = [1,3,4,4,2]
    print(Solution().findDuplicate(nums))