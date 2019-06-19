#coding:utf-8

class Solution():
    def gameOfLife(self, board):
        """

        :param board: List[List[int]]
        :return: None
        """
        self.w, self.h = len(board[0]), len(board)
        mat = [[0] * self.w for _ in range(self.h)]
        for r in range(self.h):
            for c in range(self.w):
                mat[r][c] = board[r][c]

        for r in range(self.h):
            for c in range(self.w):
                lives = self._neighborsLives(mat, (r, c))
                if lives < 2:
                    board[r][c] = 0
                if lives > 3:
                    board[r][c] = 0
                if lives == 3 and not board[r][c]:
                    board[r][c] = 1

    def _neighborsLives(self, board, node):
        count = 0
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        for i, j in neighbors:
            if 0 <= node[0] + i < self.h and 0 <= node[1] + j < self.w:
                count += board[node[0] + i][node[1] + j] & 1

        return count

if __name__ == '__main__':
    board = [ [0,1,0],
              [0,0,1],
              [1,1,1],
              [0,0,0]]
    Solution().gameOfLife(board)
    print(board)