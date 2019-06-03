#coding:utf-8

class Solution():
    def merge(self, nums1, m, nums2, n):
        """

        :param nums1: List[int]
        :param m: int
        :param nums2: List[int]
        :param n: int
        :return: None
        """
        nums1[m : m + n] = nums2[ : n]
        nums1.sort()

def main():
    test = Solution()
    nums1 = [1,2,3,0,0,0]
    nums2 = [2, 5, 6]
    m = 3
    n = 3
    test.merge(nums1, m, nums2, n)
    print(nums1)

if __name__ == '__main__':
    main()