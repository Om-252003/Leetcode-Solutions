class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        totals = []
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                ans= ans+nums[i]
            else:
                totals.append(ans)

                ans = nums[i]
        if ans>0:
            totals.append(ans)

        return max(totals)