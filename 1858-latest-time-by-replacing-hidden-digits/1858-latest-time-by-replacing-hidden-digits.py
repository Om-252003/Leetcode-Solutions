class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        s=list(time)
        for i in range(len(s)):
            if s[i]=='?':
                if i==0:
                    if s[i+1] in ['0','1','2','3','?']:
                        s[i]='2'
                    else:
                        s[i]='1'
                elif i==1:
                    if s[i-1]=='1' or s[i-1]=='0':
                        s[i]='9'
                    else:
                        s[i]='3'
                elif i==3:
                    s[i]='5'
                elif i==4:
                    s[i]='9'
        return ''.join(s)