#coding:utf-8

class Solution():
    def isMonotonic(self, A):
        """

        :param A: List[int]
        :return: bool
        """
        if sorted(A) == A or sorted(A) ==  A[::-1]:
            return True
        else:
            return False


def main():
    test = Solution()
    A = [1, 2, 3, 3, 4]
    B = [3, 4, 2, 1, 5]
    C = [5, 4, 3, 2, 1]
    print(test.isMonotonic(A))
    print(test.isMonotonic(B))
    print(test.isMonotonic(C))

if __name__ == '__main__':
    main()