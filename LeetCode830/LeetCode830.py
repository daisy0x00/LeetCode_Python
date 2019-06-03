#coding:utf-8

import re

class Solution():
    def largeGroupPositions(self, S):
        """

        :param S: str
        :return: List[List[int]]
        """
        li = re.compile(r'(([a-zA-Z])\2*)').findall(S)
        start = 0
        res = []
        for e in li:
            l = len(e[0])
            if l >= 3:
                res.append([start, start + l - 1])
            start += l
        return res

def main():
    test = Solution()
    S = "abcdddeeeeaabbbcd"
    print(test.largeGroupPositions(S))


if __name__ == '__main__':
    main()

# [[3,5],[6,9],[12,14]]