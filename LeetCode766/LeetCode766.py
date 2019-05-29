#coding:utf-8

class Solution():
    def isToeplitzMatrix(self, matrix):
        """

        :param matrix:  List[List[int]]
        :return: bool
        """

        for i in range(len(matrix) - 1):
            for j in range(len(matrix[0]) - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True


def main():
    test = Solution()
    matrix1 = [[1, 2],
              [2, 2]]
    matrix2 = [[1,2,3,4],
              [5,1,2,3],
              [9,5,1,2]]
    print(test.isToeplitzMatrix(matrix1))
    print(test.isToeplitzMatrix(matrix2))


if __name__ == '__main__':
    main()