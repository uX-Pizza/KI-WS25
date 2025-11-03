class Board:
    def __init__(self, board):
        self.board = board
        self.children = []
        self.player1 = "X"
        self.player2 = "O"
        self.value = self.utility()


    def free_spaces(self):
        return [i for i in range(0, 9) if self.board[i] == " "]


    def utility(self):
        win_states = [
            [self.board[0], self.board[1], self.board[2]],
            [self.board[3], self.board[4], self.board[5]],
            [self.board[6], self.board[7], self.board[8]],
            [self.board[0], self.board[3], self.board[6]],
            [self.board[1], self.board[4], self.board[7]],
            [self.board[2], self.board[5], self.board[8]],
            [self.board[0], self.board[4], self.board[8]],
            [self.board[6], self.board[4], self.board[2]]
        ]

        if [self.player1, self.player1, self.player1] in win_states:
            return 1
        elif [self.player2, self.player2, self.player2] in win_states:
            return -1
        elif len(self.free_spaces()) == 0:
            return 0
        else:
            return None


    def print(self):
        print("-------------")
        for i in range (0, 9):
            if i % 3 == 0 and i != 0:
                print("|")
            print(f"| {self.board[i]} ", end="")
        print("|\n-------------")