import random
import os

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
    os.system("cls" if os.name == "nt" else "clear")
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
    os.system("cls" if os.name == "nt" else "clear")
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
        self.board = [['O' for x in range(self.size[1])] for y in range(self.size[0])]
        self.guess = []
        self.miss = []
        self.boat_placement = []
    
    def print(self): 
        for row in self.board:
            print(" ".join(row))

    def random_boat_selection(self):
        index1 = self.size[0] - 1
        index2 = self.size[1] - 1
        print(f'Index 1: {index1}, Index 2: {index2}')
        for boat in range(self.boats):
            while True:
                rand1 = random.randint(0, index1)
                rand2 = random.randint(0, index2)
                if self.validate_boat_placement(rand1, rand2):
                    print(f"Boat nº {boat + 1} placed!")
                    print(f"row = {rand1}, col = {rand2}")
                    self.board[rand1][rand2] = 'X'
                    break

        print(f"All {self.boats} boats placed!")

    def manual_boat_placement(self):
        print("Choose the location of the boats.")
        print("Remember, you're grid is composed of: ")
        print(f"{self.size[0]} rows.")
        print(f"{self.size[1]} columns.\n")
        
        for boat in range(self.boats):
            while True:
                while True:
                    print(f"Choose row to place boat (Must be between 1 and {self.size[0]}")
                    row_selection = input()
                    if self.validate_integer_input(row_selection):
                        if self.validate_integer_range(int(row_selection)):
                            break

                while True:
                    print(f"Choose column to place boat (Must be between 1 and {self.size[1]}")
                    column_selection = input()
                    if self.validate_integer_input(column_selection):
                        if self.validate_integer_range(int(column_selection)):
                            break

                if self.validate_boat_placement(int(row_selection), int(column_selection)):
                    print(f"Boat nº {boat + 1} placed!")
                    self.board[int(row_selection)][int(column_selection)] = 'X'
                    break
                else: 
                    print("There's already a boat in the location:")
                    print(f"Row:{row_selection}. Column: {column_selection} ")

    def validate_integer_input(self, data):
        try:
            check_data = int(data)
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
            return False
        return True
            
    def validate_integer_range(self, data):   
        try:
            if self.size[0] <= data or data <= 0:
                raise ValueError(
                f"Value must be between {self.size[0]} and 0, you provided {data}"
                )       
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
            return False
        return True    

    def validate_boat_placement(self, row, col):
    
        coordinates = [row, col]
        for boat in self.boat_placement:
            if coordinates == boat:
                return False  
        self.boat_placement.append(coordinates)            
        return True
        
            
    
def main():
    welcome_function()
    board_size = input_board_size()
    fleet_size = input_fleet_size()
    user_board= Board(board_size, fleet_size)
    # computer_board = board(board_size)
    user_board.print()
    user_board.manual_boat_placement()
    user_board.print()



main()
