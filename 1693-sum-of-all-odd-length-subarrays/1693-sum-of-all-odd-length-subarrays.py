class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        total, n = 0, len(arr)
        for i in range(n):
            times = ((i+1)*(n-i)+1)//2
            total += times * arr[i]
        return total