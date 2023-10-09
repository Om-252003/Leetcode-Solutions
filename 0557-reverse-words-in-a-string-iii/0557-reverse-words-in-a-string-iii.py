class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s1=""
        cnt=0
        list1=[]
        demo=list(s.split(" "))

        for i in demo:
            list1.append(i[::-1])

        for j in range(len(list1)):
            if cnt == 0:
                s1 += "" + list1[j]
                cnt+=1
            else: s1 += " " + list1[j]

        return s1