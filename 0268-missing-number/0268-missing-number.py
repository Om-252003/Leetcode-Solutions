class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt=0
        for i in range(0,(len(nums)+1)):
            if i in nums:
                cnt+=1
            else: 
                return i