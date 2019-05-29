#coding:utf-8

class Solution():
    def sortArrayByParity(self, A):
        """

        :param A: List[int]
        :return: List[int]
        """

        return sorted(A, key = lambda x: x % 2)

def main():
    A = [3, 1, 2, 6, 4]
    test = Solution()
    print(test.sortArrayByParity(A))

if __name__ == '__main__':
    main()