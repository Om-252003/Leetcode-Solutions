class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        cnt = 0
        maxi = 0
        for num in nums:
            if num == 1:
                cnt += 1
                maxi = max(maxi, cnt)
            elif num == 0:
                cnt = 0

        return maxi