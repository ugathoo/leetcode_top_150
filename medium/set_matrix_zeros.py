## PROBLEM #73 Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's. You must do it in place.

## NOTES: Space complexity must be O(1) [in-place requirement]. 

## APPROACH Overview: Need a list of flags of some sort to say whether a row or column needs to be set to 0.

## Approach 1: 2 sets of flags, one for rows and one for columns. Downside: O(mn) time complexity.

## Approach 2: Go "diagonally". Once each row and column is checked, move diagonally inwards and repeat. Use the first row and column as flags.

class Solution(object):
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        first_set = False

        #set flags using first row and column as flagsets
        for i in range(rows):
            if matrix[i][0] == 0:
                first_set = True
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        #iterate through matrix again, and if flag is set to 0, set element to 0
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(cols):
                matrix[0][i] = 0

        if first_set:
            for i in range(rows):
                matrix[i][0] = 0

## Final Time Complexity: O(m + n) -> only iterating through matrix 2x, visiting each cell only once per iteration for a total of 2m + 2n times
## Final Space Complexity: O(1) -> Changing matrix in place with 1 extra variable
        