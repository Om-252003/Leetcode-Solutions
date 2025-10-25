class Solution:
    def totalMoney(self, n: int) -> int:
        k=1
        sum = 0
        count = 1
        for i in range(1,n+1):
            if (count > 7) and ((count-1) % 7 == 0):
                k = (count//7 ) + 1
            
            sum+=k
            k+=1
            count +=1
        return sum