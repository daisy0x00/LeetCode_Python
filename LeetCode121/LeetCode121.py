#coding:utf-8

class Solution():
    def maxProfit(self, prices):
        """

        :param prices: List[int]
        :return: int
        """
        if len(prices) < 2:
            return 0

        profit = 0
        minimum = prices[0]

        for i in prices:
            minimum = min(i, minimum)
            profit = max(i - minimum, profit)
        return profit

def main():
    test = Solution()
    prices = [7, 2, 3, 4, 5, 6, 1]
    print(test.maxProfit(prices))

if __name__ == '__main__':
    main()