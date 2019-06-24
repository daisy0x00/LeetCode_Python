#coding:utf-8

class Solution():
    def minPathSum(self, grid):
        """

        :param grid: List[List[int]]
        :return: int


        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                dp[i][j] = grid[i][j]

        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0 and j - 1 >= 0:
                    dp[i][j] += min(dp[i - 1][j], dp[i][j - 1])
                elif i - 1 >= 0:
                    dp[i][j] += dp[i - 1][j]
                elif j - 1 >= 0:
                    dp[i][j] += dp[i][j - 1]
        return dp[-1][-1]
        """

        if not grid:
            return 0

        mem = grid[0][:]
        r, c = len(grid), len(grid[0])
        for i in  range(1, c):
            mem[i] += mem[i - 1]
        for j in range(1, r):
            mem[0] += grid[j][0]
            for i in range(1, c):
                mem[i] = min(mem[i - 1], mem[i]) + grid[j][i]

        return mem[-1]

if __name__ == '__main__':
    grid = [[1,3,1],
            [1,5,1],
            [4,2,1]]

    print(Solution().minPathSum(grid))
