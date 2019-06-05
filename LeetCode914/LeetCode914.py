#coding:utf-8

from collections import Counter
class Solution():
    def hasGroupSizeX(self, deck):
        """

        :param deck: List[int]
        :return: bool
        """
        count = Counter(deck)
        X = min(count.values())
        for x in range(2, X + 1):
            if all(v % x == 0 for v in count.values()):
                return True
        return False

def main():
    test = Solution()
    deck = [1,1,1,1,2,2,2,2,2,2]
    print(test.hasGroupSizeX(deck))

if __name__ == '__main__':
    main()