class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        newnums = []
       
        while len(nums) != 1:
            for i in range(len(nums)-1):
                newnums.append((nums[i]+nums[i+1]) % 10)
            nums = newnums
            newnums = []
        return nums[0]


