#coding:utf-8

class Solution():
    def fib(self, N):
        """

        :param N: int
        :return: int
        """
        a, b = 0, 1
        for i in range(N):
            a, b = b, a + b
        return a

def main():
    test = Solution()
    print(test.fib(11))

if __name__ == '__main__':
    main()