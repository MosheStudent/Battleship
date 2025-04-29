import random
import Board

class Ship:
    def __init__(self, boatSize, orientation, board, index):
        #make sure to enforce that board is an object type Board ^

        self.boatSize = boatSize
        self.orientation = orientation #true for vertical
        self.board = board
        self.index = index

    def placeShip(self):
        self.checklimits()
        
        if self.orientation:
            for cells in range(self.index[1], self.index[1] + self.boatSize):
                self.board.matrix[self.index[0]][cells] = '#'
            
        else:
            for cells in range(self.index[0], self.index[0] + self.boatSize):
                self.board.matrix[cells][self.index[1]] = '#'

    def checklimits(self): #only for walls
        cell = self.board.CELL - 1
        row = self.board.ROW - 1 

        if self.orientation:
            if (self.index[1] + (self.boatSize - 1) > row):
                self.index[1] = self.index[1] - ((self.index[1] + self.boatSize - 1) - row)
                print(self.index)
        else:
            if (self.index[0] + self.boatSize - 1 > cell):
                self.index[0] = self.index[0] - ((self.index[1] + self.boatSize - 1) - row)
                print(self.index)


board = Board.Board(10,10)
boat = Ship(5, False, board, [0,2])
boat.placeShip()
board.drawBoard()



#small ship = 2 cells, 4 items

#medium ship = 3 cells, 3 items

#large ship = 4 cells, 2 items

#Huge ship = 6 cells, 1 items