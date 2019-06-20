#coding:utf-8

class Solution():
    def rotate(self, matrix):
        """

        :param matrix: List[List[int]]
        :return: None
        """

        matrix[:] = [ list(i) for i in zip(*matrix[::-1])]

if __name__ == '__main__':
    matrix = [[1,2,3],
              [4,5,6],
              [7,8,9]]

    Solution().rotate(matrix)
    print(matrix)