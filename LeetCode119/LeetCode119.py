#coding:utf-8

class Solution():
    def getRow(self, rowIndex):
        """

        :param rowIndex: int
        :return: List[int]
        """

        triangle = []

        for row_num in range(rowIndex + 1):
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1


            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

            triangle.append(row)

        return triangle[-1]

def main():
    test = Solution()
    print(test.getRow(3))

if __name__ == '__main__':
    main()