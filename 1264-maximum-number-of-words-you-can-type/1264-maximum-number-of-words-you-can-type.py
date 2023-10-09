class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        ans = 0
        
        for i in text.split(" "):
            for j in i:
                if j in brokenLetters:
                    ans -= 1
                    break
            ans += 1

        return ans