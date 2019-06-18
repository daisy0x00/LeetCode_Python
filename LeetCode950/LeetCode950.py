#coding:utf-8

from collections import deque

class Solution():
    def deckRevealedIncreasing(self, deck):
        """

        :param deck: List[int]
        :return: List[int]
        """

        res = deque()
        deck.sort(reverse = True)
        for card in deck:
            res.rotate()
            res.appendleft(card)

        return list(res)

def main():
    test = Solution()
    deck = [17,13,11,2,3,5,7]
    print(test.deckRevealedIncreasing(deck))

if __name__ == '__main__':
    main()