class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for i in range(0,len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]*2==arr[j] or arr[i]==arr[j]*2:
                    return True;
        return False;