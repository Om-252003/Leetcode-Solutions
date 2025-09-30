class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        start = 0
        end = row*col -1
        while(start<=end):
            mid = start + int((end-start)/2)
            element = matrix[int(mid/col)][int(mid%col)]
            if(element==target): return True
            elif(target<element): end = mid-1
            else: start = mid+1
        
        return False

        