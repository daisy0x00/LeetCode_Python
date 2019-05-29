#coding:utf-8

class Solution():
    def removeElement(self, nums, val):
        """

        :param nums: List[int]
        :param val: int
        :return: int
        """

        val_nums = nums.count(val)
        for _ in range(val_nums):
            nums.remove(val)

        return len(nums)

def main():
    test = Solution()
    nums = [1, 3, 2, 3, 4]
    print(test.removeElement(nums, 3))

if __name__ == '__main__':
    main()