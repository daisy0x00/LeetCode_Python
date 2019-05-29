#coding:utf-8

from string import ascii_lowercase
from collections import Counter

class Solution():
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        row = None
        col = None

        for i in range(len(board)):
            if "R" in board[i]:
                row = i
                break
        col = board[row].index("R")

        count = 0
        for i in board[row][col + 1 :]:
            if i == '.':
                pass
            elif i == 'B':
                break
            elif i == 'p':
                count += 1
                break

        for i in board[row][col - 1 :: -1]:
            if i == '.':
                pass
            elif i == 'B':
                break
            elif i == 'p':
                count += 1
                break

        s = ''.join(i[col] for i in board)

        pos = s.index("R")

        for x in s[pos + 1 :]:
            if x == '.':
                pass
            elif x == 'B':
                break
            elif x == 'p':
                count += 1
                break

        for x in s[pos - 1 :: -1]:
            if x == '.':
                pass
            elif x == 'B':
                break
            elif x == 'p':
                count += 1
                break
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