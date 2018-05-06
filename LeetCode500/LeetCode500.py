# codinng:utf-8

class Solution(object):
    def findWords(self,words):
        """

        :param words: List[str]
        :return:      List[str]
        """

        dict = {'z':1,'x':1,'c':1,'v':1,'b':1,'n':1,'m':1,
                'a':2,'s':2,'d':2,'f':2,'g':2,'h':2,'j':2,'k':2,'l':2,
                'q':3,'w':3,'e':3,'r':3,'t':3,'y':3,'u':3,'i':3,'o':3,'p':3}

        return list(filter(lambda y:y,map(lambda word:word if len(set([dict[k] for k in word.lower()])) == 1 else False,words)))

def main():
    words = ["Hello","Alaska","Dad","Peace"]
    test = Solution()
    print(test.findWords(words))

if __name__ =='__main__':
    main()
