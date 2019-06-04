#coding:utf-8
# 题目希望从数组中找出连续k个数组成的子数组，要求其平均数最大，其实就是操作滑动距离为1的滑动窗口
# note1：此处，平均数最大等价于和最大，所以中途运算时不需要算平均数，只需要在最后结果处除以k。
# note2：由于数组中存储的是整数，所以直接拿和除以k得到的数字还是整数，要对求得的和进行强制类型转换。
# note3：由于前后滑动窗之间大部分元素相同，所以没必要大量重复运动（会超时）。窗口滑动，只需要将离开窗口的元素减掉，再将新进入窗口的元素加上即可。


class Solution():
    def findMaxAverage(self, nums, k):
        """

        :param nums: List[int]
        :param k: int
        :return: float
        """
        length = len(nums)
        if k == length:
            return sum(nums) * 1.0 / length
        lastSum = sum(nums[:k])
        maxSum = lastSum
        for i in range(k, length):
            sumNums = lastSum + nums[i] - nums[i - k]
            if sumNums > maxSum:
                maxSum = sumNums
            lastSum = sumNums

        return maxSum * 1.0 / k



def main():
    test = Solution()
    nums = [1,12,-5,-6,50,3]
    nums1 = [0,1,1,3,3]
    k = 4
    print(test.findMaxAverage(nums, k))
    print(test.findMaxAverage(nums1, k))


if __name__ == '__main__':
    main()
