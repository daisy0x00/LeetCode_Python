#coding:utf-8

class Solution():
    def maximumProduct(self, nums):
        """

        :param nums: List[int]
        :return: int
        """
        if len(nums) < 3:
            return 0
        numsSorted = sorted(nums)
        result1 = numsSorted[-1] * numsSorted[-2] * numsSorted[-3]
        result2 = numsSorted[0] * numsSorted[1] * numsSorted[-1]
        return max(result1, result2)

def main():
    test = Solution()
    nums = [-9, -8, 5, 6, 10]
    print(test.maximumProduct(nums))

if __name__ == '__main__':
    main()