class Ship:
    def __init__(self, boatSize, orientation, board, index):
        #make sure to enforce that board is an object type Board ^

        self.boatSize = boatSize
        self.isHorizontal = orientation 
        self.board = board
        self.index = index

        self.fixed_index = self.checklimits()
        self.indices = []

        self.findIndices()

    def findIndices(self): #returns a list of all the indexes the ship occupies
        row, cell = self.index

        if self.isHorizontal:
            for index in range(cell, cell + self.boatSize):
                self.indices.append([row, index])
        else:
            for index in range(row, row + self.boatSize):
                self.indices.append([index, cell])


    def placeShip(self):
        row, cell = self.index

        if self.isHorizontal:
            for cells in range(cell, cell + self.boatSize):
                self.board.matrix[row][cells] = '#'
            
        else:
            for cells in range(row, row + self.boatSize):
                self.board.matrix[cells][cell] = '#'

    def checklimits(self): #only for walls
        cell = self.board.CELL - 1
        row = self.board.ROW - 1 

        if self.isHorizontal:
            if (self.index[1] + (self.boatSize - 1) > row):
                self.index[1] = self.index[1] - ((self.index[1] + self.boatSize - 1) - row)
        else:
            if (self.index[0] + self.boatSize - 1 > cell):
                self.index[0] = self.index[0] - ((self.index[1] + self.boatSize - 1) - row)

    def shoot(self, tag): #shoot algorithm
        index = self.board.tagToIndex(tag)

        if self.board.matrix[index] == '#':
            self.board.matrix[index] = 'X'
            print("\n>>> HIT!")




