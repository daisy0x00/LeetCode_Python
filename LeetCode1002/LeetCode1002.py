#coding:utf-8

from string import ascii_lowercase
from collections import Counter

class Solution():
    def commonChars(self, A):
        """

        :param A: List[str]
        :return:  List[str]
        """
        d = list()
        for i in A:
            # d返回的是一个字典
            d.append(Counter(i))
            print(d)
        res = list()
        # 遍历a-z
        for c in ascii_lowercase:
            tmp = 100
            # i表示d里面的key值，即例子例子里面包含的字母
            for i in d:
                #
                if c in i:
                    tmp = min(i[c], tmp)
                    print('c,i[c]: ', c, i[c])
                else:
                    tmp = 0
                    break
            for j in range(tmp):
                res.append(c)
        return res

def main():
    A = ['bella', 'label', 'roller']
    B = ['cool', 'lock', 'cook']
    test = Solution()

    print(test.commonChars(A))
    print(test.commonChars(B))

if __name__ == '__main__':
    main()