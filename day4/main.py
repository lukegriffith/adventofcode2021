
class structure():
    def __init__(self, f):
        data = f.readlines()
        self.boards = []
        self.virtual_boards = []
        self.coord_set = {}
        board_buffer = []
        for i, v in enumerate(data):
            line = v.strip('\n')
            if i == 0:
                self.bingo_numbers = line 
                continue
            if line == '':
                if len(board_buffer) == 0:
                    continue
                self.boards.append(board_buffer.copy())
                self.virtual_boards.append(self.create_virtual_board())
                board_buffer = []
            if line != '':
                numbers = line.split(None, 4)
                board_buffer.append(numbers)
        self.boards.append(board_buffer.copy())
        self.virtual_boards.append(self.create_virtual_board())

        for i, board in enumerate(self.boards):
            for x in range(5):
                for y in range(5):
                    val = int(self.boards[i][x][y])
                    if val not in self.coord_set:
                        self.coord_set[val] = []
                    self.coord_set[val].append((i,x,y))


    def create_virtual_board(self):
        return [
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
        ]

def main(input_f):
    with open(input_f) as f:
        s = structure(input_f)
        # STRUCTURE HAS A VIRTAUL BOARD, FROM BINGO NUMBERS
        # CHECK THE COORD MAP AND UPDATE THE COORDS
        # THEN SCAN BOARD, USE TRANSPOSE FOR VERTICAL FINDING ONLY TRUES
        # IF LENGTH OF TRUES == 5, YOU GOT A WINNER


if __name__ == '__main__':
    print(main('sample_input.txt'))
