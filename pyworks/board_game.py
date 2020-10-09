class BoardGame:
    def __init__(self):
        self.board=["1", "2", "3",
                    "4", "5", "6",
                    "7", "8", "9"]
    
    def print_board(self):
        print("|".join(self.board[0: 3]))
        print("-+-+-")
        print("|".join(self.board[3: 6]))
        print("-+-+-")
        print("|".join(self.board[6: 9]))

    def evaluate(self):
        self.win = False
        if self.board[0] == self.board[1] and self.board[1] == self.board[2]:
            self.win = True
        if self.board[3] == self.board[4] and self.board[4] == self.board[5]:
            self.win = True
        if self.board[6] == self.board[7] and self.board[7] == self.board[8]:
            self.win = True
        if self.board[0] == self.board[3] and self.board[3] == self.board[6]:
            self.win = True
        if self.board[1] == self.board[4] and self.board[4] == self.board[7]:
            self.win = True
        if self.board[2] == self.board[5] and self.board[5] == self.board[8]:
            self.win = True
        if self.board[0] == self.board[4] and self.board[4] == self.board[8]:
            self.win = True
        if self.board[2] == self.board[4] and self.board[4] == self.board[6]:
            self.win = True

    def game(self):
        mark = "O"
        for _ in range(9):
            self.print_board()
            input_num = input("{}をどこに入れますか？".format(mark))
            self.board[int(input_num) - 1] = mark
            self.evaluate()
            if self.win == True:
                print(f"{mark}が揃いました {mark}の勝ちです")
                break
            if mark == "O":
                mark = "X"
            else:
                mark = "O"
        else:
            self.print_board()
            print("引き分けです")

a=BoardGame()
a.game()
        
