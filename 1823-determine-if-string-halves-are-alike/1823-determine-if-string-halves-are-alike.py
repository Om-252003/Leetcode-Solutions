class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        halfA  = s[:len(s)//2 ]                    
        halfB  = s[ len(s)//2:]                    

        vowels = 'aeiouAEIOU'

        countA = sum(ch in vowels for ch in halfA)  
        countB = sum(ch in vowels for ch in halfB)  
        return countA == countB   