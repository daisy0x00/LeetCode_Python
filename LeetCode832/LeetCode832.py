#coding:utf-8

class Solution():
   # def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
    def flipAndInvertImage(self, A):
        """
        :param A: List[List[int]]
        :return: List[List[int]]
        """

        # row[::-1]使用了切片性质将列表逆序
        A = [row[::-1] for row in A]
        # lambda是匿名函数
        # map(function, Iterable)将函数function作用于Iterable中的每个元素并返回Iterable
        A = [list(map(lambda x: 1-x, row)) for row in A]

        return A


def main():
    A = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    B = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    test = Solution()

    print(test.flipAndInvertImage(A))
    print(test.flipAndInvertImage(B))


if __name__ == '__main__':
        main()