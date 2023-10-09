class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """

        l1=list(s1.split())
        l2=list(s2.split())
        ans=[]

        for i in l1:
            if i not in l2:
                if l1.count(i) < 2:
                    ans.append(i)


        for j in l2:
            if j not in l1:
                if l2.count(j) < 2:
                    ans.append(j)


        return ans