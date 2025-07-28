class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        r,w,b= nums.count(0), nums.count(1), nums.count(2)
        index=0
        for i in range(r):
            nums[i] = 0
        for i in range(r, r+w):
            nums[i] =1
        for i in range(r+w, r+w+b):
            nums[i]=2

        



       
