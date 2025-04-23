class Board:
    def __init__(self):
        self.ROW = 10
        self.CELL = 10   

        self.matrix = [[0]*self.ROW for i in range(self.CELL)]

        #tags for row and cell:
        self.tagLetters = ['A','B','C','D','E','F','G','H','I','J']
        self.tagNumbers = list(range(1,self.ROW + 1))

    def tagToIndex(self, tag):
        newIndex = [0,0]
        
        newIndex[0] = self.tagLetters.index(tag[0], 0, len(self.tagLetters))
        newIndex[1] = self.tagNumbers.index(tag[1], 0, len(self.tagNumbers))

        return newIndex
    
    def indexToTag(self, index):
        newTag = [0,0]

        newTag[0] = self.tagLetters[index[0]]
        newTag[1] = self.tagNumbers[index[0]]

        return newTag
 

    def drawBoard(self):
        ROW = 0

        first = True

        for letter in self.tagLetters:
            print(f'\t{letter}', end="")
            
        print('\n')

        for row in self.matrix:
            if not first:
                print('\n')
            

            print(f'{self.tagNumbers[ROW]}  \t', end="")
            ROW += 1


            for cell in row:
                print(f'{cell} \t', end="")

            first = False
