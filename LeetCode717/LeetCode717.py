#coding:utf-8

# 解题思路：从左到右遍历。遇到0下标增1，遇到1下标增2，然后判断最后下标若为n-1则返回TRUE

class Solution():
    def isOneBitCharacter(self, bits):
        """

        :param bits: List[int]
        :return: bool
        """
        length = len(bits)
        count = 0
        while count < length:
            if count == length - 1:
                return True
            elif bits[count] == 0:
                count += 1
            else:
                count += 2

        return False

def main():
    test = Solution()
    bits = [1, 0, 0]
    bits1 = [1, 1, 1, 0]
    print(test.isOneBitCharacter(bits))
    print(test.isOneBitCharacter(bits1))

if __name__ == '__main__':
    main()


