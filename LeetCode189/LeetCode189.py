#coding:utf-8

# 先一半一半的旋转，然后再整个旋转，最后实现向右移动的效果
class Solution():
    def rotate(self, nums, k):
        """

        :param nums: List[int]
        :param k: int
        :return: None
        """
        turns = k % len(nums)
        middle = len(nums) - turns
        self.reverse(nums, 0, middle - 1)
        self.reverse(nums, middle, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)


    def reverse(self, nums, l, r):
        while r  > l:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

def main():
    test = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3
    test.rotate(nums, k)
    print(nums)

if __name__ == '__main__':
    main()



