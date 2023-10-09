class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = b = 0
        for i, c in enumerate(s):
            if i % 2 == 0:
                if c == '0':
                    a += 1
                else:
                    b += 1
            else:
                if c == '0':
                    b += 1
                else:
                    a += 1
        
        return min(a, b)