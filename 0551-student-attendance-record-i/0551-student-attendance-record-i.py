class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """

        A1, L1 = 0, 0
        for i in range(len(s)):
            if A1 > 1 or L1 > 2:
                return False
            if s[i] == 'A':
                A1 += 1
                L1=0
            elif s[i] == 'L':
                L1 += 1
               
            else:
                L1 = 0

        if A1 <2 and L1<3 : return True