# coding:utf-8

class Solution:
    def uniqueMorseRepresentations(self,words):
        """

        :param words: list[str]
        :return:      int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        mapping = dict(zip([chr(i) for i in range(ord('a'),ord('z') + 1,1)],morse))

        return len(set(map(lambda word:''.join(mapping[k] for k in word),words)))

       # trans = ''.join([mapping[k] for k in words])
       # trans = list(map(''.join(list(lambda word:mapping[k] for k in word)),words))

        #return trans


def main():

    words = ["gin", "zen", "gig", "msg"]

    test = Solution()

    print(test.uniqueMorseRepresentations(words))

if __name__ == '__main__':
    main()
