class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=bin(n).replace('0b','')
        t=''
        for i in s:
            if i=='0':
                t+='1'
            else:
                t+='0'
        return int(t,2)
