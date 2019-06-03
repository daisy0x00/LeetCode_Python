#coding:utf-8

class Solution():
    def plusOne(self, digits):
        """

        :param digits: List[int]
        :return: List[int]
        """
        intNum = 0
        for i in range(len(digits)):
            intNum = intNum * 10 + digits[i]
        intNum += 1
        strNum = str(intNum)
        res = []
        for i in range(len(strNum)):
            res.append(int(strNum[i]))

        return res

def main():
    test = Solution()
    digits = [1, 2, 3]
    digits1=  [9]
    print(test.plusOne(digits))
    print(test.plusOne(digits1))

if __name__ == '__main__':
    main()
