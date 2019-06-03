#coding:utf-8

class Solution():
    def canThreePartsEqualSum(self, A):
        """

        :param A: List[int]
        :return: bool
        """
        tmp = sum(A) / 3
        res = 0
        count = 0
        for i in range(len(A)):
            res += A[i]
            if res == tmp:
                count += 1
                res = 0
        if count == 3:
            return True
        else:
            return False

def main():
    test = Solution()
    A = [0,2,1,-6,6,7,9,-1,2,0,1]
    B = [3,3,6,5,-2,2,5,1,-9,4]
    print(test.canThreePartsEqualSum(A))
    print(test.canThreePartsEqualSum(B))

if __name__ == '__main__':
    main()