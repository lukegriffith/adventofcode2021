from numpy import transpose

class NoWinnerException(Exception):
    pass

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

    def winner(self):
        for i, b in enumerate(self.virtual_boards):
            row_trues = [len([y for y in i if y == True]) for i in b ]
            if 5 in row_trues:
                return i
            column_trues = [len([y for y in i if y == True]) for i in transpose(b)]
            if 5 in column_trues:
                return i
        raise NoWinnerException("No winner") 
            

def main(input_f):
    winner = None
    with open(input_f) as f:
        s = structure(f)
        last_bingo_number = None
        # STRUCTURE HAS A VIRTAUL BOARD, FROM BINGO NUMBERS
        # CHECK THE COORD MAP AND UPDATE THE COORDS
        # THEN SCAN BOARD, USE TRANSPOSE FOR VERTICAL FINDING ONLY TRUES
        # IF LENGTH OF TRUES == 5, YOU GOT A WINNER
        for number in list(map(int, s.bingo_numbers.split(","))):
            last_bingo_number = number
            try:
                for coords in s.coord_set[number]:
                    i,x,y = coords
                    s.virtual_boards[i][x][y] = True
            except KeyError:
                pass
            try:
                winner = s.winner()
            except NoWinnerException:
                print("No winner this time") 

            if winner  != None:
                break
        if winner == None:
            raise NoWinnerException("No Winner after bingo numbers processed")

        winning_board = s.boards[winner]
        winning_board_matrix = s.virtual_boards[winner]
        unmarked_sum = 0
        for i, v in enumerate(winning_board_matrix):
            for x, v in enumerate(v):
                if winning_board_matrix[i][x] == False:
                    unmarked_sum += int(winning_board[i][x])
        return unmarked_sum * last_bingo_number
        

if __name__ == '__main__':
    print(main('sample_input.txt'))
    print(main('input.txt'))
