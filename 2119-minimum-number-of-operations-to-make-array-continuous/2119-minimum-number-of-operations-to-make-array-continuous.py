class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = n
        hash_set = set()
    
        for x in nums:
            hash_set.add(x)
    
        unique = list(hash_set)
        unique.sort()
    
        j = 0
        m = len(unique)
    
        for i in range(m):
            while j < m and unique[j] < unique[i] + n:
                j += 1
            ans = min(ans, n - j + i)
    
        return ans