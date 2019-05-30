#coding:utf-8

class Solution():
    def findDisappeardNumbers(self, nums):
        """

        :param nums: List[int]
        :return: List[int]
        """

        #nums_only = set(nums)
        #nums_all = set(list(range(1, len(nums) + 1)))
        #result = list(nums_all - nums_only)
        #return result

        return list(set(range(1, len(nums) + 1)) - set(nums))

def main():
    test = Solution()
    nums = [2, 3, 2, 4, 5, 7, 7]
    print(test.findDisappeardNumbers(nums))

if __name__ == '__main__':
    main()
