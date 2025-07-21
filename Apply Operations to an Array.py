class Solution(object):
    def applyOperations(self, nums): 
        i=0
        length= len(nums)
        while i < length -1:
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] *2 
                nums[i+1] =0 

            i+=1
        
        result= []
        zero_count = 0

        for num in nums:
            if num !=0:
                result.append(num)
            else:
                zero_count+=1

        for _ in range(zero_count):
            result.append(0)

        return result
        


            
    """
        :type nums: List[int]
        :rtype: List[int]
        """
        
