class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 1
        prev = 1
        for i in nums:
            if i + prev < 1:
                ans += 1 - ( i + prev )
                prev = 1
            else:
                prev = i + prev
        return ans