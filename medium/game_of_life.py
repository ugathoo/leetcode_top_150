## PROBLEM #289: According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
                ## The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). 
                ## Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
                ## Any live cell with fewer than two live neighbors dies as if caused by under-population.
                ## Any live cell with two or three live neighbors lives on to the next generation.
                ## Any live cell with more than three live neighbors dies, as if by over-population.
                ## Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
                ## The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.
                ## Given the current state of the board, update the board to reflect its next state.

## Approach 1: If 0 -> 1, mark in-place as 2. If 1 -> 0, mark in place as -1. Key here is realizing I am not limited to 0s and 1s when it comes to changing numbers. At the end, iterate through the board and if number is 2, change to 1. If number is -1, change to 0.
class Solution(object):

    def getNeighbors(self, board, i, j):
        neighbors = 0
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                if x == i and y == j:
                    continue #skip current cell
                if x < 0 or x >= len(board):
                    continue #skip out of bounds
                if y < 0 or y >= len(board[0]):
                    continue #skip out of bounds
                if board[x][y] == 1 or board[x][y] == -1:
                    neighbors += 1 #live neighbor
        return neighbors
    
    def gameOfLife(self, board):
        #Rules:
            # 1. Any live cell with less than 2 neighbors = 1 or -1 dies.
            # 2. Any live cell with 2 or 3 neighbors = 1 or -1 lives.
            # 3. Any live cell with more than 3 neighbors = 1 or -1 dies.
            # 4. Any dead cell with 3 neighbors = 1 or -1 lives.
        
        r = len(board)
        c = len(board[0])
        
        for i in range(r):
            for j in range(c):
                neighbors = self.getNeighbors(board, i, j)
                if board[i][j] == 1:
                    if neighbors < 2 or neighbors > 3:
                        board[i][j] = -1
                else:
                    if neighbors == 3:
                        board[i][j] = 2


        #change cells
        for i in range(r):
            for j in range(c):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == -1:
                    board[i][j] = 0
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        