# coding:utf-8

class Solution(object):
    def moveZeroes(self,nums):
        """

        :param nums: List[int]
        :return:     void Do not return anything,modify nums in-place instead.
        """
        for index,item in enumerate(nums):
            if item == 0:
                for i in range(index + 1,len(nums)):
                    if nums[i] != 0:
                        nums[i],nums[index] = nums[index],nums[i]
                        break


#        for i in range(len(nums) - 1):
#            for j in range(len(nums) - i - 1):
#                if nums[j] == 0:
 #                   nums[j],nums[j + 1] = nums[j + 1],nums[j]




def main():
    nums = [0,0,1]
    test = Solution()
    test.moveZeroes(nums)
    print(nums)

if __name__ =='__main__':
    main()