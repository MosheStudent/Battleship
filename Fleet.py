import Ship

class Fleet: #creates all the boats on the board
    def __init__(self, board):
        self.sizes = [2,3,3,4,5]
        self.originalShips= len(self.sizes)

        self.ships = [] # list of boats

        self.board = board

    def place_boats(self):
        for size in self.sizes:
            index = [0,0]
            index[1] = int(input("\n>>> Enter index X: "))
            index[0] = int(input("\n>>> Enter index Y: ")) 

            isHorizontal = input("\n>>> Horizontal?(Y/N): ")

            if isHorizontal == 'Y':
                isHorizontal = True
            else:
                isHorizontal = False


            newShip = Ship.Ship(size, isHorizontal, self.board, index)
            newShip.checklimits()



            while self.isCollide(newShip):
                print("\n>>> Enter a valid index!!!\n")

                index[1] = int(input("\n>>> Enter index X: "))
                index[0] = int(input("\n>>> Enter index Y: ")) 

                newShip = Ship.Ship(size, isHorizontal, self.board, index)

                newShip.checklimits()


            self.ships.append(newShip)
            newShip.placeShip()

            self.board.drawBoard()
            
        
    def isCollide(self, newShip):
        occupied = newShip.indices
        index = [0,0]


        for row in self.board.matrix:
            index[1] = 0

            for cell in row:
                #if cell == '#':
                if index in occupied and cell == '#':
                    return True

                index[1] += 1
            index[0] += 1

    def shoot(self, tag): #shoot algorithm
        index = self.board.tagToIndex(tag)

        if self.board.matrix[index] == '#':
            self.board.matrix[index] = 'X'
            print("\n>>> HIT!")

            row, cell = 0

            #remove index from boat from list:
            for ship in self.ships:
                for cell in ship:
                    if (cell == index):
                        del self.ships[row, cell]

                    cell += 1
                
                row += 1
                cell = 0

            
        if len(self.ships) < self.originalShips:
            print('\n>>> SUNK!')

            self.originalShips = len(self.ships)

        if self.ships == []:
            print('\n>>> WINNER!!!')
            








