import random
import os


def title():
    """
    Print hangman title.
    """
    print("\033[1;34m")
    print("BATTLESHIP".center(80, "-"))
    print("\n")


def welcome_function():
    """
    Welcome function which salutes the user
    """
    print("version, you will play against the machine,")
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

#good idea to eliminate
def validate_boat_fleet(data):
    """
    Validates fleet size data by converting data into integer. 
    Raises value error if value entered is not between 3 and 8.
    Also raises a value error if the value is not an integer.
    """
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
        """
        Prints the board in user friendly style. 
        The location of the boats are visible.
        """
        for boat in self.boat_placement:
            self.board[boat[0]][boat[1]] = '@'
        for guess in self.guess:
            self.board[guess[0]][guess[1]] = 'X'
        for miss in self.miss:
            self.board[miss[0]][miss[1]] = '0'
        for row in self.board:
            print(" ".join(row))
        

    def enemy_print(self):
        """
        Prints the board without displaying the location of the boats 
        that haven't been hit
        """
        for guess in self.guess:
            self.board[guess[0]][guess[1]] = 'X'
        for miss in self.miss:
            self.board[miss[0] - 1][miss[1]] = '0'
        for row in self.board:
            print(" ".join(row))
        

    def random_boat_selection(self):
        """
        Inputs a random boat selection that can be used by the user 
        and always by the enemy
        """
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
        """
        Permits the user to select the location of the boats.
        User has to enter all the locations manually
        """
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
        """
        Validates if the input is an intenger.
        Used multiple times throught the creation of the board:
        -Validation of the location of the boats
        -Validation of the shot during the game.
        """
        try:
            check_data = int(data)
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
            return False
        return True
            
    def validate_integer_range(self, data, size): 
        """
        Validates if an integer is inside a range.
        Used multiple times throught the creation of the board:
        -Validation of the location of the boats
        -Validation of the shot during the game.  
        """
        try:
            print("\n")
            if size < data or data <= 0:
                raise ValueError(
                f"Value must be between {size} and 1 (including both), you provided {data}"
                )       
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.")
            return False
        return True    

    def validate_boat_placement(self, row, col):
        """
        Validates if the location of the boat is available
        """
        coordinates = [row, col]
        for boat in self.boat_placement:
            if coordinates == boat:
                return False  
        self.boat_placement.append(coordinates)            
        return True
        

    def input_shot_location(self):
        """
        Inputs user for the location of the desired shot
        """
        #If the column and row input are correct, but the shot has already been made,
        #the while loop will resest from the begining
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
            else:
                print("Shot has already been made! Try again.")
                

    def automatic_shot_location(self):
        """
        Automatic shooting for the enemy
        """
        index1 = self.size[0] - 1 #Converting index user friendly to python friendly
        index2 = self.size[1] - 1
        while True:
            rand1 = random.randint(0, index1)
            rand2 = random.randint(0, index2)
            if self.validate_shots_taken(rand1, rand2):
                break
            


    def validate_shots_taken(self, row, col):
        """
        Validate if the shot hits, misses or if it's already been made
        """
        if [row, col] in self.guess:
            return False
        elif [row, col] in self.miss:
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
    #Should I do object-oriented method?
    #Asks for inputs about the number of boats and size of the boards
    board_size = input_board_size()
    fleet_size = input_fleet_size()
    
    #Creates the boards for the enemy and the user
    user_board= Board(board_size, fleet_size)
    enemy_board = Board(board_size, fleet_size)


    #Add boats on the boards
    user_board.manual_boat_placement()
    enemy_board.random_boat_selection()
    os.system("cls" if os.name == "nt" else "clear")

    #Game mechanics: stops the game when a player has won (or there is a draw)
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
            #Displays the boards
            print("User board:")
            user_board.user_print()
            print("\n")
            print("Enemy board:")
            enemy_board.user_print()
            print("\n")
            
            print(f"Your last shot was: {enemy_board.last_shot}\n ")
            print(f"Last enemy shot was: {user_board.last_shot}\n\n ")

            #Stops the loop at this points, asking for location of next shot.
            enemy_board.input_shot_location()
            user_board.automatic_shot_location()
            os.system("cls" if os.name == "nt" else "clear")



main()