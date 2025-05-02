import Board
import Fleet
import Ship

class main:
    def __init__(self):
        self.BOARDSIZE = 10
        self.RUNNING = True

        self.board_p1 = Board.Board(self.BOARDSIZE, self.BOARDSIZE)
        self.board_p2 = Board.Board(self.BOARDSIZE, self.BOARDSIZE)

        self.radar_board_p1 = Board.Board(self.BOARDSIZE, self.BOARDSIZE)
        self.radar_board_p2 = Board.Board(self.BOARDSIZE, self.BOARDSIZE)
 
        self.fleet_p1 = Fleet.Fleet(self.board_p1)
        self.fleet_p2 = Fleet.Fleet(self.board_p2)

    def setUp(self):
        print("\np1 place boats: ")
        self.fleet_p1.place_boats()

        print("\np2 place boats: ")
        self.fleet_p2.place_boats()

        self.turns()

    def turns(self):
        while self.RUNNING:
            index_p1 = input('\np1 shoot: ')
            self.fleet_p2.shoot(index_p1)

            index_p2 = input('\np2 shoot: ')
            self.fleet_p1.shoot(index_p2)



    



mn = main()
mn.setUp()