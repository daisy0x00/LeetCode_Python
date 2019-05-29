#coding:utf-8

class Solution():
    def maxProfit(self, prices):
        """

        :param prices: List[int]
        :return: int
        """
        ans = 0
        if len(prices) <= 1:
            return 0
        for x in range(1, len(prices)):
            if prices[x] - prices[x - 1] >= 0:
                ans += prices[x] - prices[x - 1]
        return ans

def main():
    test = Solution()
    prices = [7,1,5,3,6,4]
    print(test.maxProfit(prices))

if __name__ == '__main__':
    main()