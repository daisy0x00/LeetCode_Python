#coding:utf-8

class Solution():
    def matrixReshape(self, nums, r, c):
        """

        :param nums: List[List[int]]
        :param r: int
        :param c: int
        :return: List[List[int]]
        """
        m = len(nums)
        n = len(nums[0])
        temp = []
        res = [[0 for i in range(c)] for j in range(r)]
        if m * n != r * c:
            return nums
        else:
            for i in range(m):
                for j in range(n):
                    temp.append(nums[i][j])

            for i in range(r):
                for j in range(c):
                    res[i][j] = temp[0]
                    del temp[0]

            return res


def main():
    test = Solution()
    nums = [[1, 2],
            [3, 4]]
    print(test.matrixReshape(nums, 1, 4))

if __name__ == '__main__':
    main()