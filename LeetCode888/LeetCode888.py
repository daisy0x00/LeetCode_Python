#coding:utf-8

class Solution():
    def fairCandySwap(self, A, B):
        """

        :param A: List[int]
        :param B: List[int]
        :return: List[int]
        """
        sum_A, sum_B, set_B = sum(A), sum(B), set(B)
        for a in A:
            if a + (sum_B - sum_A) / 2 in set_B:
                return [a, a + (sum_B - sum_A) / 2]

def main():
    test = Solution()
    A = [1,2,5]
    B = [2,4]
    print(test.fairCandySwap(A, B))

if __name__ == '__main__':
    main()