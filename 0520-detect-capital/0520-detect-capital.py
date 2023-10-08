class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """

        if len(word) == 1: return True

        if word[0].isupper() and word[1].isupper():
            for i in range(2, len(word)):
                if word[i].islower() : return False
            return True
            

        if word[0].isupper() and word[1].islower():
            for i in range(2,len(word)):
                if word[i].isupper(): return False
                    
            return True

        if word[0].islower() and word[1].islower():
            for i in range(2, len(word)):
                if word[i].isupper(): return False
            return True
        return False