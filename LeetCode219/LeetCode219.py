#coding:utf-8

# deque模块是python标准库collections中的一项，它提供两端都可以操作的序列
# 这意味着序列前后两端你都可以执行添加或删除操作
from collections import deque

class Solution():
    def containsNearbyDuplicate(self, nums, k):
        """

        :param nums: List[int]
        :param k: int
        :return: bool
        """
        if not nums:
            return False
        if k == 0:
            return False
        k = k + 1
        k = min(k, len(nums))

        # 创建双向队列
        window = deque()
        d = set()
        for i in range(0, k):
            if nums[i] in d:
                return True
            d |= {nums[i]}
            window.append(i)
        for i in range(k, len(nums)):
            d -= {nums[window.popleft()]}
            if nums[i] in d:
                return True
            d |= {nums[i]}
            window.append(i)
        return False

def main():
    test = Solution()
    nums = [1,2,3,1,2,3]
    k = 2
    print(test.containsNearbyDuplicate(nums, k))

if __name__ == '__main__':
    main()