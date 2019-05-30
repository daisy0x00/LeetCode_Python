#coding:utf-8

class Solution():
    def twoSum(self, nums, target):
        """

        :param nums: List[int]
        :param target: int
        :return:  List[int]


        nums_sorted = sorted(nums)
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums_sorted[left] + nums_sorted[right] == target:
                for index, num in enumerate(nums):
                    if num == nums_sorted[left]:
                        result1 = index
                    if num == nums_sorted[right]:
                        result2 = index
                return sorted([result1, result2])
            elif nums_sorted[left] + nums_sorted[right] < target:
                left += 1
            else:
                right -= 1

        return []
        """

        length = len(nums)
        dict = {}
        for x in range(length):
            a = target - nums[x]
            # 字典dict中存在nums[x]时
            if nums[x] in dict:
                return [dict[nums[x]], x]
            # 否则往字典中增加键值对
            else:
                dict[a] = x
            # 边往字典中增加键值对，边与nums[x]进行对比
def main():
    test = Solution()
    nums = [11, 7, 2, 3]
    nums1 = [3, 3]
    target = 9
    print(test.twoSum(nums, target))
    print(test.twoSum(nums1, 6))

if __name__ == '__main__':
    main()