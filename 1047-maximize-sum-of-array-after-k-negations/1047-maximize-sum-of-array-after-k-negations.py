class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        i = 0
        while k > 0:
            if i == len(nums) or nums[i] >= 0: 
                nums = sorted(nums)
                i = 0
                k = k % 2
            if k == 0: break
            nums[i] *= -1
            k -= 1
            i += 1
        return sum(nums)