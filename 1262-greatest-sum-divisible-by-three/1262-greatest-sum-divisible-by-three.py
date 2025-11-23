class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        s = sum(nums)
        
        if s % 3 == 0:
            return s
        
        r11 = 10000
        r12 = 10000
        r21 = 10000
        r22 = 10000
        
        for num in nums:
            if num % 3 == 1 and num < r12:
                if num < r11:
                    r12 = r11
                    r11 = num
                else:
                    r12 = num
            if num % 3 == 2 and num < r22:
                if num < r21:
                    r22 = r21
                    r21 = num
                else: 
                    r22 = num
        if s % 3 == 1:
            return s - min(r11, r21+r22)
        if s % 3 == 2:
            return s - min(r21, r11+r12) 