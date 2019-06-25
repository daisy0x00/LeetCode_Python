# coding:utf-8

class Solution():
    def pancakeSort(self, A):
        """

        :param A: List[int]
        :return: List[int]
        """
        res = list()
        for i in range(len(A), 1, -1):
            index = self.findMaxIndex(A[:i])
            A = A[:index][::-1] + A[index:]
            A = A[:i][::-1]
            res += [index, i]

        return res

    def findMaxIndex(self, A):
        index = 0
        for i in range(1, len(A)):
            if A[i] > A[index]:
                index = i

        return index + 1

        # res = list()
        # for i in range(len(A), 1, -1):
        #     idx = A.index(i)
        #     A = A[: idx : -1] + A[: idx]
        #     res += [idx + 1, i]
        #
        # return res


if __name__ == '__main__':
    A = [3, 2, 4, 1]
    B = [1, 2, 3]
    print(Solution().pancakeSort(A))
    print(Solution().pancakeSort(B))