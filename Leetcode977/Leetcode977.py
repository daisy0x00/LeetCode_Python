# coding:utf-8

class Solution:
    def sortedSquares(self,A):

        """

        :param A: List[int]
        :return:  List[int]
        """

        A = sorted((map(lambda x: x * x, A)))

        return A

def main():
    A = [-4, -1, 0, 3, 10]
    B = [-7, -3, 2, 3, 11]

    test = Solution()
    print(test.sortedSquares(A))
    print(test.sortedSquares(B))

if __name__ == '__main__':
    main()