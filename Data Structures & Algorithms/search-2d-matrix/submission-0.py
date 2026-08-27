class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        l = 0
        r = n - 1
        index = 0
        for i in range(len(matrix)):
            if target >= matrix[i][0]:
                if target <= matrix[i][n-1]:
                    index = i
        i = index   
        while l <= r:
            m = (l+r)//2
            if matrix[i][m] == target:
                return True
            elif matrix[i][m] > target:
                r-=1
            else:
                l+=1
        return False 