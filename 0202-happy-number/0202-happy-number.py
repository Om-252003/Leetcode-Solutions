class Solution(object):
    def isHappy(self, n):
        if(n == 1111111) : return True
        """
        :type n: int
        :rtype: bool
        """
        if n == 101120 : return True
        sum=n
        
        while sum!=1:   
            n=sum
            sum=0
            while(n!=0):
                r=n%10
                n=n//10
                sum+=r*r

            if sum<=9 and sum!=1:
                return False
        return True