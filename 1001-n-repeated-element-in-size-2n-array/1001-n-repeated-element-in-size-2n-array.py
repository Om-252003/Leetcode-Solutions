class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i+1]: return nums[i]