class Board:
    def __init__(self):
        self.grid = [[' ' for c in range(3)] for r in range(3)]

    def is_valid_move(self, pos):
        return pos[0] < 3 and pos[1] < 3 and self.grid[pos[0]][pos[1]] == ' '

    def place_move(self, pos, symbol):
        self.grid[pos[0]][pos[1]] = symbol

    def is_full(self):
        for row in self.grid:
            for place in row:
                if place == ' ':
                    return False

        return True

    def is_triplet(self):
        triplets = []
        for x in range(0, 3):
            triplets.append(self.grid[x])
            triplets.append([self.grid[0][x], self.grid[1][x], self.grid[2][x]])

        triplets.append([self.grid[0][0], self.grid[1][1], self.grid[2][2]])
        triplets.append([self.grid[0][2], self.grid[1][1], self.grid[2][0]])

        return ['X', 'X', 'X'] in triplets or ['O', 'O', 'O'] in triplets

    def is_over(self):
        return self.is_full() or self.is_triplet()

    def render(self):
        for row in self.grid:
            line = ''
            for col in row:
                line += col + '|'
            print(line[0:-1])
