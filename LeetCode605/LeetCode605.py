#coding:utf-8

# 解题思路：在数组前后 补0，然后每3个连续的0就将中间的0置1，n减去1，直到n = 0

class Solution():
    def canPlaceFlowers(self, flowerbed, n):
        """

        :param flowerbed: List[int]
        :param n: int
        :return: bool
        """
        if n == 0:
            return True
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False

def main():
    test = Solution()
    flowerbed =  [1,0,0,0,1]
    n1 = 1
    n2 = 2
    print(test.canPlaceFlowers(flowerbed, n1))
    print(test.canPlaceFlowers(flowerbed, n2))

if __name__ == '__main__':
    main()