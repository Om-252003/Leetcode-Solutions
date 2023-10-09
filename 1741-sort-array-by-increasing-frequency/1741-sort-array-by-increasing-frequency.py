class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return sorted(sorted(nums,reverse=1),key=nums.count)