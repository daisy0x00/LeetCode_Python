#coding:utf-8

class Solution():
    def dominantIndex(self, nums):
        """

        :param nums: List[int]
        :return: int
        """
        if len(nums) > 1:
            max_nums = sorted(nums)
            if max_nums[-1] >= max_nums[-2] * 2:
                return nums.index(max_nums[-1])
            return -1
        return 0

def main():
    test = Solution()
    nums = [3, 6, 1, 0]
    print(test.dominantIndex(nums))

if __name__ == '__main__':
    main()