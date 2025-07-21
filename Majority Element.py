class Solution(object):
    def majorityElement(self, nums):
        counts ={}
        for num in nums:
            if num in counts:
                counts[num] +=1
            else:
                counts[num] =1
        max_count=0
        majority= None

        for num in counts:
            if counts[num] > max_count:
                max_count = counts[num]
                majority= num
        return majority



    """
        :type nums: List[int]
        :rtype: int
        """
        
