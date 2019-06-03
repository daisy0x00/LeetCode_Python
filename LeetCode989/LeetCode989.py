# coding:utf-8

class Solution():
    def addToArrayFrom(self, A, K):
        """

        :param A: List[int]
        :param K: int
        :return: List[int]
        """

        strA = ""
        for digit in A:
            strA += str(digit)

        strResult = str(int(strA) + K)

        return [int(value) for index, value in enumerate(strResult)]

def main():
    test = Solution()
    A = [1, 2, 3, 4]
    K = 60
    print(test.addToArrayFrom(A, K))

if __name__ == '__main__':
    main()



