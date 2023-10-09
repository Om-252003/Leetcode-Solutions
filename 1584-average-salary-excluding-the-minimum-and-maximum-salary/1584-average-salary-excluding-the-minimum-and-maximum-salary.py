class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """

        avg=0.0
        salary.sort()
    
        for i in range(1,len(salary)-1): avg += salary[i]
        return avg/(len(salary)-2)