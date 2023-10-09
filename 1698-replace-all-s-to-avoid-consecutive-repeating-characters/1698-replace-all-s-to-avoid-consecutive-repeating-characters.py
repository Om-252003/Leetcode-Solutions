class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        alphabet = list(string.ascii_lowercase)
        
        notins = ''
        for i in alphabet:
            if i not in s:
                notins += i
            if len(notins) > 1: 
                break
        
        for i in notins:
            if s.count('??') > 0:
                s = s.replace('??', notins[:2]) 
            else:
                s = s.replace('?', notins[0])        
        return s