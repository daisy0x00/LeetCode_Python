# coding:utf-8

class Solution(object):
    def judgeCircle(self,moves):
        """

        :param moves: str
        :return: bool
        """
        x = 0
        y = 0

        for item in moves:
            if item == 'U':
                y = y + 1
            elif item == 'D':
                y = y - 1
            elif item == 'L':
                x = x - 1
            elif item == 'R':
                x = x + 1

        return (x == 0 and y == 0)

def main():
    moves = input("Please input moves:")
    test = Solution()
    print(test.judgeCircle(moves))

if __name__ == '__main__':
    main()