#coding:utf-8

class Solution():
    def transpose(self, A):
        """

        :param A: List[List[int]]
        :return: List[List[int]]
        """

        return [list(i) for i in zip(*A)]


def main():
    test = Solution()
    A = [[1,2,3],
         [4,5,6],
         [7,8,9]]
    print(test.transpose(A))

if __name__ == '__main__':
    main()