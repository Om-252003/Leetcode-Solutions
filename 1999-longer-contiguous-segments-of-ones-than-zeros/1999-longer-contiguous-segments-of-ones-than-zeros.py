class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return len(max(s.split('0'),key=len)) > len(max(s.split('1'),key=len))