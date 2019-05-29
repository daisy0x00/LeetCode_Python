#coding:utf-8

class Solution():
    def sumEvenAfterQueries(self, A, queries):
        """

        :param A: List[int]
        :param queries: List[List[int]]
        :return: List[int]
        """
        S = sum(x for x in A if x % 2 == 0)
        ans = []

        for x, k in queries:
            if A[k] % 2 == 0:
                S -= A[k]
            A[k] += x

            if A[k] % 2 == 0:
                S += A[k]
            ans.append(S)

        return ans


def main():
    A = [1, 2, 3, 4]
    queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
    test = Solution()
    print(test.sumEvenAfterQueries(A, queries))

if __name__ == '__main__':
    main()
