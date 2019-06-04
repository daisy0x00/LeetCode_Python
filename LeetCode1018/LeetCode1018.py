#coding:utf-8

class Solution():
    def prefixesDivBy5(self, A):
        """

        :param A: List[int]
        :return: List[bool]
        """
        res = ''
        ans = []
        for i in A:
            res += str(i)
            num = int(res, 2)
            if num % 5 == 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans

def main():
    test = Solution()
    A = [0,1,1,1,1,1]
    print(test.prefixesDivBy5(A))

if __name__ == '__main__':
    main()
