from copy import deepcopy
import random

class Game:
    def __init__(self):
        self.board = [["_","_","_"],
                     ["_","_","_"],
                     ["_","_","_"]]

    def printBoard(self):
        print [0,"0","1","2"]
        print [0]+self.board[0]
        print [1]+self.board[1]
        print [2]+self.board[2]

    def computerMove(self):
        self.board = deepcopy(random.choice(self.possibleNextMoves()))

    def playerMove(self,row,column):
        self.board[row][column] = "O"

    def possibleNextMoves(self):
        result = []
        for row in range(3):
            for column in range(3):
                if self.board[row][column] == "_":
                    newBoard = deepcopy(self.board)
                    newBoard[row][column] = "x"
                    result.append(newBoard)
        return result

    def gameFinished():
        

if __name__ == '__main__':
    game = Game()
    while(True):
        game.printBoard()
        user_input = raw_input("Please enter your move (row,column) ")
        row,column = user_input.split(",")
        game.playerMove(int(row),int(column))

        print "computers turn"
        game.computerMove()
