from board import Board
from player import Player

class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Player('X')
        self.player2 = Player('O')

    def play_game(self):
        players = [self.player1, self.player2]
        turn = 0
        while (not self.board.is_over()):
            self.board.render()
            current_player = players[turn % 2]
            move = current_player.make_move()
            if self.board.is_valid_move(move):
                self.board.place_move(move, current_player.symbol) 
                turn += 1
            else:
                print('Invalid move')

        self.board.render()
        print('Game over')
