import random

def welcome_function():
    """
    Welcome function which salutes the user
    """
    print("Welcome to this exciting match of the classic battleship game!")
    print("In this version, you will play against the machine, you will have the chance to choose how big you want your board and how many ships you would like.")
    # adding a path to instructions functions


def input_board_size():
    """
    Inputs the user to choose the board size
    """
    board_size = []
    print("Now you will choose the size of the board.\n")
    while True:
        print("Please, choose number of rows (3 to 6):")
        row = input()
        if validate_board_size(row):
            board_size.append(int(row))
            break

    while True:
        print("Please, choose number of columns (3 to 6):")
        col = input()
        if validate_board_size(col):
            board_size.append(int(col))
            break

    return board_size




def validate_board_size(data):
    """
    Validates board size data by converting data into integer. 
    Raises value error if value entered is not between 1 and 8.
    Also raises a value error if the value is not an integer.
    """
    try:
        check_data = int(data)
        if check_data >= 7 or check_data <= 2:
            raise ValueError(
                f"Value must be between 3 and 6, you provided {check_data}"
            )
        
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True


def input_fleet_size():

    print("Choose the number ships per user.\n")
    while True:
        print("Please, choose between 3 to 8:") 
        boats = input()
        if validate_boat_fleet(boats):
            print("Number of boats is valid!")
            break

    return int(boats)

def validate_boat_fleet(data):
    try:
        check_data = int(data)
        if check_data >= 9 or check_data <= 2:
            raise ValueError(
                f"Value must be between 3 and 8, you provided {check_data}"
            )       
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True

class Board:
    """
    Class that creates the boards for the user and the enemy
    """
    def __init__(self, size, boats):
        self.size = size
        self.boats = boats
        self.board = [['O' for x in range(self.size[1]+1)] for y in range(self.size[0])]
    
    def print(self): 
        for row in self.board:
            print(" ".join(row))  
        print(self.size)
        print(self.board)

    def random_boat_selection(self):
        index1 = self.size[0]
        index2 = self.size[1]

        for boat in range(self.boats):
            rand1 = random.randint(0, index1)
            rand2 = random.randint(0, index2)
            self.board[rand1][rand2] = 'X'

            

def main():
    welcome_function()
    board_size = input_board_size()
    fleet_size = input_fleet_size()
    user_board= Board(board_size, fleet_size)
    # computer_board = board(board_size)
    user_board.print()
    user_board.random_boat_selection()
    user_board.print()



main()
