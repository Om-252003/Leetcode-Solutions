class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        for i in word:
            if i.isalpha():
                word = word.replace(i, "_")
            listx = word.split("_")
        listx = [int(i) for i in listx if i!=""]
        return len(set(listx))