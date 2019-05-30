#coding:utf-8

from collections import Counter

class Solution():
    def findShortestSubArray(self, nums):
        """

        :param nums: List[int]
        :return: int
        """

        c = Counter(nums)
        first = {}
        last = {}
        for i, v in enumerate(nums):
            first.setdefault(v, i)
            last[v] = i
        degree = max(c.values())

        return min(last[v] - first[v] + 1 for v in c if c[v] == degree)


def main():
    test = Solution()
    nums = [1,2,2,3,1,4,2]
    print(test.findShortestSubArray(nums))

if __name__ == '__main__':
    main()