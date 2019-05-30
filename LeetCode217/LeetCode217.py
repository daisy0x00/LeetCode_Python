#coding:utf-8

class Solution():
    def containsDuplicate(self, nums):
        """

        :param nums: List[int]
        :return: bool
        """
        if len(list(set(nums))) != len(nums):
            return True
        else:
            return False


def main():
    test = Solution()
    nums = [1, 2, 3, 4]
    print(test.containsDuplicate(nums))

if __name__ == '__main__':
    main()
