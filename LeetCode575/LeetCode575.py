# coding:utf-8

class Solution(object):
    def distributeCandies(self,candies):
        """

        :param candies: List[int]
        :return:        int
        """

        return int(len(candies) / 2) if len(set(candies)) >= len(candies) / 2 else len(set(candies))

def main():
    candies = [1,1,2,3,4,5]
    test = Solution()
    print(test.distributeCandies(candies))

if __name__ == '__main__':
    main()