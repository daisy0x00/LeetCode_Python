#coding:utf-8

from string import ascii_lowercase
from collections import Counter

class Solution():
    def matrixReshape(self, nums, r, c):
        row = len(nums)
        col = len(nums[0])

        tmp = []
        res = [[0 for i in range(c)] for j in range(r)]

        for i in range(row):
            for j in range(col):
                tmp.append(nums[i][j])

        for i in range(r):
            for j in range(c):
                res[i][j] = tmp[0]
                del tmp[0]

        return res


def main():
    test = Solution()
    nums = [[1, 2, 3],
            [4, 5, 6]]
    print(test.matrixReshape(nums, 6, 1))

if __name__ == '__main__':
    main()