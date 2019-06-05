#coding:utf-8

class Solution():
    def numMagicSquaresInside(self, grid):
        """

        :param grid: List[List[int]]
        :return: int


        l = [[8, 1, 6, 3, 5, 7, 4, 9, 2],
             [6, 1, 8, 7, 5, 3, 2, 9, 4],
             [4, 9, 2, 3, 5, 7, 8, 1, 6],
             [2, 9, 4, 7, 5, 3, 6, 1, 8],
             [6, 7, 2, 1, 5, 9, 8, 3, 4],
             [8, 3, 4, 1, 5, 9, 6, 7, 2],
             [2, 7, 6, 9, 5, 1, 4, 3, 8],
             [4, 3, 8, 9, 5, 1, 2, 7, 6]]
        count = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                tmp = grid[i][j : j + 3] + grid[i + 1][j : j + 3] + grid[i + 2][j : j + 3]
                if tmp in l:
                    count += 1
        return count
        ###
        这个方法有问题，有待修改
        ###
        row = len(grid)
        col = len(grid[0])

        if row < 3 or col < 3:
            return 0
        sum = 0
        for i in range(row - 2):
            for j in range(col - 2):
                if grid[i][j] ==5 and self.isLawfulNum(grid, j, i):
                    sum += 1
                    j += 2
                else:
                    j += 1
        return sum

        def isLawfulNum(self, grid, x, y):


        :param grid: List[List[int]]
        :param x: int
        :param y: int
        :return: bool

        num1 = grid[y - 1][x - 1]
        num2 = grid[y - 1][x]
        num3 = grid[y][x - 1]
        num4 = grid[y - 1][x + 1]
        num5 = grid[y][x + 1]
        num6 = grid[y + 1][x - 1]
        num7 = grid[y + 1][x]
        num8 = grid[y + 1][x + 1]
        if num1 %5 != 0 and num2 % 5 != 0 and num3 % 5 != 0 and num4 % 5 != 0:
            if 10 - num1 == num8 and 10 - num2 == num7 and 10 - num3 == num5 and 10 - num4 == num6:
                return True
        return False
        """
        count = 0
        if len(grid)<3 or len(grid[0])<3: return count # 小于3*3，直接返回0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                ul, um, ur = grid[i][j], grid[i][j+1], grid[i][j+2]
                ml, mm, mr = grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2]
                dl, dm, dr = grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]
                nums = [ul, um, ur, ml, mm, mr, dl, dm, dr]
                if sorted(nums) != [1,2,3,4,5,6,7,8,9]:
                    continue # 如果九个数不为1-9，跳过当前循环
                elif ul+um+ur==15 and ml+mm+mr==15 and dl+dm+dr==15 and ul+ml+dl==15 and um+mm+dm==15 and ur+mr+dr==15 and ul+mm+dr==15 and ur+mm+dl==15: # 计算每行、每列、对角线的八个和
                    count += 1

        return count

def main():
    test = Solution()
    grid = [[4,3,8,4],
            [9,5,1,9],
            [2,7,6,2]]
    grid1 = [[1,1,1],
             [4,5,6],
             [9,9,9]]
    print(test.numMagicSquaresInside(grid))
    print(test.numMagicSquaresInside(grid1))

if __name__ == '__main__':
    main()
