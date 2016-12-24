class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self):
        move  = input('Please enter the move you want to make as row space col. ex/ 1 2: ')
        move = move.split()
        return [int(move[0]), int(move[1])]
