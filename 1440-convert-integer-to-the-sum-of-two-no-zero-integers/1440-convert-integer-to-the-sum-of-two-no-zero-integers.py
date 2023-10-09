class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # s=[n//2]
        # s.append(n-s[0])
        if not '0' in str(n-1):
                    return [n-1,1]
        else:
            k=1
            while '0' in str(n-k) or '0' in str(k):
                k+=1
            return [n-k,k]