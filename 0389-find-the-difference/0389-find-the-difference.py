class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        s1=list(s)
        t1=list(t)

        for char in t1:
            if char in s1:
                s1.remove(char)
            elif char not in s1:
                return char