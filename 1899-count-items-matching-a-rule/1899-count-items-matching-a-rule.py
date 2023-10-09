class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        count=0
        if ruleKey=="type":
            j=0
        elif ruleKey=="color":
            j=1
        else:
            j=2
        for i in range(len(items)):
            if ruleValue==items[i][j]:
                count+=1
        return count