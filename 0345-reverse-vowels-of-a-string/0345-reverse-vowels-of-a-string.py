class Solution:
    def reverseVowels(self, s: str) -> str:
        l1 = list(s)
        vowels = "aeiouAEIOU"
        i,j = 0,len(l1)-1
        while (i<j):
            
            while i<j and vowels.find(l1[i]) == -1:
                i = i+1
            
            while i<j and vowels.find(l1[j]) == -1:
                j=j-1

            l1[i],l1[j] = l1[j],l1[i]
            i+=1
            j-=1
                    
        return "".join(l1)
        