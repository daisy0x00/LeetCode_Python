#coding:utf-8

class Solution():
    def numRookCaptures(self, board):
        """

        :param board: List[List[str]]
        :return: int
        """
        # 找到R所在的行和列

        # 对记录R所在的行和列进行初始化
        row = None
        col = None
        # R所在的行
        for x in range(len(board)):
            if "R" in board[x]:
                row = x
                break
        # R所在的列
        col = board[row].index("R")
        # count用来记录车能够捕获的所有的卒，给count赋初值为0
        count = 0
        # 从R的位置开始向右出发，寻找这个方向上捕获的卒
        for i in board[row][col + 1 :]:
            if i == ".":
                pass
            elif i == "B":
                break
            elif i == "p":
                count += 1
                break

        # 从R的位置开始向左出发，寻找这个方向上捕获的卒
        for i in board[row][col - 1 :: -1]:
            if i == ".":
                pass
            elif i == "B":
                break
            elif i == "p":
                count += 1
                break
		# R所在的列的所有列元素
        s = ''.join(i[col] for i in board)
		# R在列的索引位置
        pos = s.index("R")

        # 从R的位置开始向上出发，寻找这个方向上捕获的卒
        for x in s[pos + 1 :]:
            if x == ".":
                pass
            elif x == "B":
                break
            elif x == "p":
                count += 1
                break
        # 从R的位置向下出发，寻找这个方向上捕获的卒
        for x in s[pos - 1::-1]:
            if x == ".":
                pass
            elif x == "B":
                break
            elif x == "p":
                count += 1
                break
        # 返回能够捕获的卒的总数量
        return count

def main():
    test = Solution()
    board = [[".",".",".",".",".",".",".","."],
             [".",".",".","p",".",".",".","."],
             [".",".",".","R",".",".",".","p"],
             [".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".",".","."],
             [".",".",".","p",".",".",".","."],
             [".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".",".","."]]

    print(test.numRookCaptures(board))

if __name__ == '__main__':
    main()
