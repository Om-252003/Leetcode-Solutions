class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        return nums == sorted(nums) or nums == sorted(nums, reverse=True)