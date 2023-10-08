class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        demo = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in demo:
                return [demo[diff], i]
            else:
                demo[nums[i]] = i