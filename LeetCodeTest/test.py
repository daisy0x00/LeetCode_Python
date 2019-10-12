class Solution():
    def test(self, heights):
        len_heights = len(heights)
        heights_sorted = sorted(heights)
        count = 0

        for i in range(len_heights):
            if heights[i] != heights_sorted