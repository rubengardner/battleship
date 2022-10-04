import random
import os

def welcome_function():
    """
    Welcome function which salutes the user
    """
    print("Welcome to this exciting match of the classic battleship game!")
    print("In this version, you will play against the machine,")
    print("you will have the chance to choose the size of the board and the amount of ships.")
    # adding a path to instructions functions


def input_board_size():
    """
    Inputs the user to choose the board size and 
    returns the value as a list of two integers
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
    Raises value error if value entered is not between 3 and 6.
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
    """
    Inputs user to specify the number of boats per board. (Between 3 and 8)
    """
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
        self.board = [['*' for x in range(self.size[1])] for y in range(self.size[0])]
        self.guess = []
        self.miss = []
        self.boat_placement = []
        self.last_shot='No last shot'
    
    def user_print(self): 
        for boat in self.boat_placement:
            self.board[boat[0]][boat[1]] = '@'
        for guess in self.guess:
            self.board[guess[0]][guess[1]] = 'X'
        for miss in self.miss:
            self.board[miss[0]][miss[1]] = '0'
        for row in self.board:
            print(" ".join(row))
        

    def enemy_print(self):
        for guess in self.guess:
            self.board[guess[0]][guess[1]] = 'X'
        for miss in self.miss:
            self.board[miss[0] - 1][miss[1]] = '0'
        for row in self.board:
            print(" ".join(row))
        

    def random_boat_selection(self):
        index1 = self.size[0] - 1 #Converting index user friendly to python friendly
        index2 = self.size[1] - 1
        
        for boat in range(self.boats):
            while True:
                rand1 = random.randint(0, index1)
                rand2 = random.randint(0, index2)
                if self.validate_boat_placement(rand1, rand2):
                    break

        print(f"All {self.boats} boats placed!")

    def manual_boat_placement(self):
        print("Choose the location of the boats.")
        print("Remember, you're grid is composed of: ")
        print(f"{self.size[0]} rows.")
        print(f"{self.size[1]} columns.\n")
        
        for boat in range(self.boats):
            while True:
                print(f"Please, input boat nº {boat + 1} coordinates:")
                while True:
                    print(f"Row (Must be between 1 and {self.size[0]}):")
                    row_selection = input()
                    if self.validate_integer_input(row_selection):
                        if self.validate_integer_range(int(row_selection), self.size[0]):
                            break

                while True:
                    print(f"Column(Must be between 1 and {self.size[1]}):")
                    column_selection = input()
                    if self.validate_integer_input(column_selection):
                        if self.validate_integer_range(int(column_selection), self.size[1]):
                            break

                if self.validate_boat_placement(int(row_selection) - 1, int(column_selection) - 1):
                    os.system("cls" if os.name == "nt" else "clear")
                    print(f"Boat nº {boat + 1} placed!\n")
                    break
                else: 
                    os.system("cls" if os.name == "nt" else "clear")
                    print("There's already a boat in that location:")
                    print(f"Row:{row_selection}. Column: {column_selection}\n ")

        os.system("cls" if os.name == "nt" else "clear")
        print("All boats placed correctly!")

    def validate_integer_input(self, data):
        try:
            check_data = int(data)
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
            return False
        return True
            
    def validate_integer_range(self, data, size):   
        try:
            if size < data or data <= 0:
                raise ValueError(
                f"Value must be between {size} and 1 (including both), you provided {data}"
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
        

    def input_shot_location(self):

        while True:
            while True:
                print("Let's fire!")
                print(f"Choose a row between 1 and {self.size[0]}: ")  
                row_shooting = input()
                if self.validate_integer_input(row_shooting):
                    row_shooting = int(row_shooting)
                    if self.validate_integer_range(row_shooting, self.size[0]):
                        break
                           
            while True:
                print(f"Choose a column between 1 and {self.size[1]}: ")  
                col_shooting = input()
                if self.validate_integer_input(col_shooting):
                    col_shooting= int(col_shooting)
                    if self.validate_integer_range(col_shooting, self.size[0]):
                        break
                            
            if self.validate_shots_taken(row_shooting - 1, col_shooting - 1):
                break
               
    def automatic_shot_location(self):
        index1 = self.size[0] - 1 #Converting index user friendly to python friendly
        index2 = self.size[1] - 1
        while True:
            rand1 = random.randint(0, index1)
            rand2 = random.randint(0, index2)
            if self.validate_shots_taken(rand1, rand2):
                break
            


    def validate_shots_taken(self, row, col):
        if [row, col] in self.guess:
            print('You already shot this location')
            return False
        elif [row, col] in self.miss:
            print('You already shot this location')
            return False
        elif [row, col] in self.boat_placement:
            self.last_shot = 'HIT!'
            self.guess.append([row ,col])
            return True
        else:
            self.last_shot = "Miss"
            self.miss.append([row, col])
            return True
  
def main():
    welcome_function()
    board_size = input_board_size()
    fleet_size = input_fleet_size()
    
    user_board= Board(board_size, fleet_size)
    enemy_board = Board(board_size, fleet_size)


    user_board.manual_boat_placement()

    enemy_board.random_boat_selection()
    
    os.system("cls" if os.name == "nt" else "clear")
    while True:
        if len(enemy_board.guess) == fleet_size and len(user_board.guess) == fleet_size:
            print("Draw")
            return False
        elif len(enemy_board.guess) == fleet_size:
            print("Win")
            return False
        elif len(user_board.guess) == fleet_size:
            print("Loose")
            return False
        else:
            print("User board:")
            user_board.user_print()
            print(f"Last enemy shot was: {user_board.last_shot} ")
            print("\n")
            print("Enemy board:")
            enemy_board.user_print()
            print(f"Your last shot was: {enemy_board.last_shot} ")
            enemy_board.input_shot_location()
            user_board.automatic_shot_location()
            os.system("cls" if os.name == "nt" else "clear")



main()