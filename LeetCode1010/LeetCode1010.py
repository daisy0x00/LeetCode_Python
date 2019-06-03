#coding:utf-8
from collections import Counter

# 题目给了每个数的上限为500， 所以两数之和的上限为1000， 因此可以只要在1000以内的60的倍数里找就行了
# 先统计一下每个数出现的频率，然后记录在record这个数组中
# 缺点：比较慢
class Solution():
    def numPairsDivisibleBy60(self, time):
        """

        :param time: List[int]
        :return: int
        """
        record = [i * 60 for i in range(1, 18) if i ^ 60 <= 1000]
        dic = Counter(time)

        res = 0
        for item in time:
            for check in record:
                tmp = check - item
                if item == tmp:
                    res += dic[tmp] - 1
                else:
                    res += dic[tmp]

        return res // 2

def main():
    test = Solution()
    time = [30,20,150,100,40]
    time1 = [30, 30, 30]
    print(test.numPairsDivisibleBy60(time))
    print(test.numPairsDivisibleBy60(time1))

if __name__ == '__main__':
    main()