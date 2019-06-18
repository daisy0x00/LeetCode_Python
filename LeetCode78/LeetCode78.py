#coding:utf-8

class Solution():
    def subsets(self, nums):
        """

        :param nums: List[int]
        :return: List[List[int]]
        """

        res = [[]]
        for num in nums:
            for temp in res[:]:
                x = temp[:]
                x.append(num)
                res.append(x)
        return res

def main():
    test = Solution()
    nums = [1, 2, 3]
    print(test.subsets(nums))

if __name__ =='__main__':
    main()