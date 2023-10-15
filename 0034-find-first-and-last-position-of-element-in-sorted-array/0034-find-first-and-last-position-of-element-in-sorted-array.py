class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = -1  
        last = -1   
    
        for i in range(len(nums)):
            if nums[i] == target:
                if first == -1:
                    first = i 
                last = i
        
       
        return [first, last]