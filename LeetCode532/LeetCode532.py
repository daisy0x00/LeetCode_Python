#coding:utf-8

# 解题思路：先对数组排序，然后使用滑动窗口遍历数组，因为数组排序之后差是可以连续移动的两个指针得到的，这种方法同样要对相同的数字进行排除
class Solution():
    def findPairs(self, nums, k):
        """

        :param nums: List[int]
        :param k: int
        :return: int
        """
        sortedNums = sorted(nums)
        count = 0
        left = 0
        right = 1
        while right < len(sortedNums):
            firNum = sortedNums[left]
            secNum = sortedNums[right]
            if secNum - firNum < k:
                right += 1
            elif secNum - firNum > k:
                left +=1
            else:
                count += 1
                while left < len(sortedNums) and sortedNums[left] == firNum:
                    left += 1
                while right < len(sortedNums) and sortedNums[right] == secNum:
                    right += 1
            if right == left:
                right += 1
        return count

def main():
    test = Solution()
    nums = [3, 1, 4, 1, 5]
    k = 2
    nums1 = [1,3,1,5,4]
    k1 = 0
    print(test.findPairs(nums, k))
    print(test.findPairs(nums1, k1))

if __name__ == '__main__':
    main()

