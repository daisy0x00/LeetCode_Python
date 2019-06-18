#coding:utf-8

class Solution():
    def  generateMatrix(self, n):
        """

        :param n: int
        :return: List[List[int]]
        """

        A = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(1, n**2 + 1):
            A[i][j] = k
            if A[(i + di) % n][(j + dj) % n]:
                di, dj = dj, -di

            i += di
            j += dj

        return A

def main():
    test = Solution()
    n = 3
    #print(test.generateMatrix(n))

if __name__ == '__main__':
    main()