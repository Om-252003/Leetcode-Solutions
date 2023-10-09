class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=1
        c=1
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                c=c+1
            else:
                res=max(res,c)
                c=1
        res=max(res,c)
        return res