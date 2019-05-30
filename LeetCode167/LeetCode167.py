#coding:utf-8

# 对撞指针法，双索引法
# 我们首先判断首尾两项的和是不是target，如果比target小，那么我们将左边+1的位置再和右边相加，继续判断
# 如果比target 大，那么我们将右边-1的位置和左边相加，继续判断。我们通过这样不断地缩放过程，就可以在
# O(n)的时间复杂度找到对应的位置坐标（这和快速排序的思路很相似）
class Solution():
    def twoSum(self, numbers, target):
        """

        :param numbers: List[int]
        :param target: int
        :return: List[int]
        """
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return[left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        return []


def main():
    test = Solution()
    numbers = [2, 7, 11, 15]
    target = 18
    print(test.twoSum(numbers, target))

if __name__ == '__main__':
    main()

