class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        demo=[]
        s=""

        for n in num:
            s = s+str(n)
        s = int(s)
        s=s+k
       
        s = str(s)

        for i in range(len(s)):
            t=int(s[i])
            demo.append(t)

        return demo