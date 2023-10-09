class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i=0
        demo=list(bin(n))
        demo.pop(0)
        demo.pop(0)

        while i+1<(len(demo)):

            if demo[i] == demo[i+1] :
                return False
            i+=1
        return True