class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        money = 0
        j = 1
        for i in range(1, n+1):
            if i % 7 == 1:
                j = i // 7 + 1
            
            money += j
            j += 1
    
        return money 