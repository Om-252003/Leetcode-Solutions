class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        spaces = 0
        for i in text:
            if i==" ":
                spaces+=1
        words = text.split()
        num_words = len(words)
        if num_words==1:
            return words[0]+(" "*spaces)
        space = spaces//(num_words-1)
        extra= spaces%(num_words-1)
        ans=""
        for i in words:
            ans+=i
            ans+=space*" "
        ans=ans[:-space]
        ans+=extra*" "
        return ans