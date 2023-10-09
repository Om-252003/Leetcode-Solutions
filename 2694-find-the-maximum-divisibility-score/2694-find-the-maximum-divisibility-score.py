class Solution(object):
    def maxDivScore(self, nums, divisors):
        """
        :type nums: List[int]
        :type divisors: List[int]
        :rtype: int
        """
        divisors.sort()
        max=0
        res=divisors[0]
        for i in range(len(divisors)):
            cnt=0
            for j in range(len(nums)):
                if (nums[j] % divisors[i] == 0):
                    cnt+=1
            if cnt>max:
                max=cnt
                res=divisors[i]
        return res