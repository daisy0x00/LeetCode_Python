# coding:utf=8

class Solution():
    def minCostClimbingStairs(self, cost):
        """

        :param cost: List[int]
        :return: int
        """
        dp0 = cost[0]
        dp1 = cost[1]
        for i in range(2, len(cost)):
            dpi = min(dp0 + cost[i], dp1 + cost[i])
            dp0 = dp1
            dp1 = dpi
        return min(dp0, dp1)

def main():
    test = Solution()
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(test.minCostClimbingStairs(cost))

if __name__ == '__main__':
    main()