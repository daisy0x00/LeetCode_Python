#coding:utf-8

# deque模块是python标准库collections中的一项，它提供两端都可以操作的序列
# 这意味着序列前后两端都可以执行添加或删除操作
from collections import deque

class Solution():
    def containsNearbyDuplicate(self, nums, k):
        """

        :param nums: List[int]
        :param k: int
        :return: bool
        """
        # 1.先判断nums是否为空为空则返回FALSE。再判断k是否等于0，为0则返回FALSE
        if not nums:
            return False
        if k == 0:
            return False

        # 2.由于range函数后面的取值范围取不到则需要k + 1,然后需要判断加1后的k有什么超过nums的长度
        # 若超过，则选择nums的长度作为k值。
        k = k + 1
        k = min(k, len(nums))

        # 3.定义了一个双向队列windows来存储元素的下标，一个集合d来存储元素
        window = deque()
        d = set()

        # 4.先从下标0开始取元素并判断是否已经存在d中，由于我们的下标范围是0~k + 1，若存在d中，则说明有满足条件的i和j.
        # 若不存在则将该元素加入d，依次循环直到结束。
        for i in range(0, k):
            if nums[i] in d:
                return True
            d |= {nums[i]}
            window.append(i)

        # 5.若此次循环并没有找到，则开始第二个循环。由于要满足i和j的绝对值最大为k,
        # 每次循环前我们需要删除d中一个元素，我们可以根据windows所存下标依次删除。
        # 然后再判断之后的元素是否在d中，若存在d中，则说明有满足条件的i和j。
        # 若不存在则将该元素加入d， 依次循环直到循环结束。
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
    print(test.containsNearbyDuplicate(nums, k))#False

if __name__ == '__main__':
    main()
