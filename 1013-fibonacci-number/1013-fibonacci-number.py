class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        f1, f2 = 0, 1
        temp=[0,1]
        sum=0
        for i in range(n):
            f3 = f1 + f2
            f1,f2=f2,f3
            temp.append(f3)
       

        sum= sum + temp[n-1] + temp[n-2]
        return sum