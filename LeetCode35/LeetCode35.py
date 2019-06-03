#coding:utf-8

class Solution():
    def searchInsert(self, nums, target):
        """

        :param nums: List[int]
        :param target: int
        :return: int
        """
        low = 0
        hight = len(nums)
        while low < hight:
            middle = int(low + (hight - low) / 2)
            if nums[middle] > target:
                hight = middle
            elif nums[middle] < target:
                low = middle + 1
            else:
                return middle
        return low

def main():
    test = Solution()
    nums = [1,3,5,6]
    target = 7
    print(test.searchInsert(nums, target))

if __name__ == '__main__':
    main()
