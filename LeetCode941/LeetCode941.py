#coding:utf-8

# 解题思路：设置左右两个指针，分别向中间靠拢，靠拢的同时要判断是不是上升过程。
# 最后判断两个指针相会点是不是有效点即可
class Solution():
    def validMountainArray(self, A):
        """

        :param A: List[int]
        :return: bool
        """
        left, right, ALength = 0, len(A) - 1, len(A)
        if ALength < 3:
            return False
        while left + 1 < ALength and A[left] <A[left + 1]:
            left += 1
        while right > 0 and A[right - 1] > A[right]:
            right -= 1

        return 0 < left == right < ALength - 1

def main():
    test = Solution()
    A = [3,5,5]
    A1 = [0,3,2,1]
    print(test.validMountainArray(A))
    print(test.validMountainArray(A1))

if __name__ == '__main__':
    main()
