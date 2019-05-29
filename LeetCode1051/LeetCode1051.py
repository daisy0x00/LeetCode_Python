#coding:utf-8

class Solution():
    def heightChecker(self, heights):
        """

        :param heights: List[int]
        :return: int
        """

        # 解题思路：将原数组排序保存到另一个数组中，然后对比这两个数组中的每一项，如果值不同，则计数器加一，最后返回计数器的值
        len_heights = len(heights)
        heights_sorted = sorted(heights)
        count = 0

        for i in range(len_heights):
            if heights[i] != heights_sorted[i]:
                count += 1

        return count

def main():
    heights = [1, 1, 4, 2, 1, 3]
    test = Solution()
    print(test.heightChecker(heights))

if __name__ == '__main__':
    main()