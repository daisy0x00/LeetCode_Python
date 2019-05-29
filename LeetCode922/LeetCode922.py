#coding:utf-8

class Solution():
    def sortArrayByParityII(self, A):
        """

        :param A: List[int]
        :return:  List[int]
        """

        result, even, odd = list(), list(), list()

        for a in A :
            if a % 2 == 0:
                even.append(a)
            else:
                odd.append(a)

        # list.pop(index)函数用于移除列表中的一个元素（默认为最后一个元素index=-1），并返回该元素的值。
        # 顺序执行result.append()就可以实现even和odd的交替
        while even and odd:
            result.append(even.pop())
            result.append(odd.pop())


        return result

def main():
    A = [4, 2, 5, 7]

    test = Solution()
    print(test.sortArrayByParityII(A))

if __name__ == '__main__':
    main()