class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        length = m*n

        l = 0
        r = length-1
        while (l<=r):
            mid = (l+r)//2
            if (matrix[mid//n][mid%n]==target):
                return True
            elif (matrix[mid//n][mid%n]<target):
                l=mid+1
            else:
                r=mid-1
        return False

