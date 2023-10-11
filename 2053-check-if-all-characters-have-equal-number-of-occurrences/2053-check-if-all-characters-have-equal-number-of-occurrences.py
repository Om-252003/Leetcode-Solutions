class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        j=[]
        for i in set(s):
            j.append(s.count(i))
        if len(set(j))!=1:
            return False
        return True