# Import random module for the random placement and shooting of boats.
import random
# Import module for the clearing of the terminal
import os


def initial_screen():
    """
    Print initial message
    """
    os.system("cls" if os.name == "nt" else "clear")
    print("\u001b[0m")
    print(
        """
        .____        _   _   _           _     _.
        | __ )  __ _| |_| |_| | ___  ___| |__ (_)_ __
        |  _ \ / _` | __| __| |/ _ \/ __| '_ \| | '_ \.
        | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |
        |____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/
                                                |_|
    """
    )
    input("Press any key:\n")


def draw_section():
    """
    Print draw message
    """
    os.system("cls" if os.name == "nt" else "clear")
    print("\u001b[0m")
    print(
        """
        .____
        |  _ \ _ __ __ ___      __
        | | | | '__/ _` \ \ /\ / /
        | |_| | | | (_| |\ V  V /
        |____/|_|  \__,_| \_/\_/
        """
    )


def loose_section():
    """
    Print loose message
    """
    os.system("cls" if os.name == "nt" else "clear")
    print("\u001b[0m")
    print(
        """
        ._
        | |    ___   ___  ___  ___ _ __
        | |   / _ \ / _ \/ __|/ _ \ '__|
        | |__| (_) | (_) \__ \  __/ |
        |_____\___/ \___/|___/\___|_|
        """
    )


def win_section():
    """
    Print win message
    """
    os.system("cls" if os.name == "nt" else "clear")
    print("\u001b[0m")
    print(
        """
        __   __                                _
        \ \ / /__  _   _  __      _____  _ __ | |
        .\ V / _ \| | | | \ \ /\ / / _ \| '_ \| |
        . | | (_) | |_| |  \ V  V / (_) | | | |_|
        . |_|\___/ \__,_|   \_/\_/ \___/|_| |_(_)
        """
    )


def title():
    """
    Print title.
    """
    # clear terminal
    os.system("cls" if os.name == "nt" else "clear")
    print("\033[1;37m")
    print("BATTLESHIP".center(80, "-"))
    print("\n")


def welcome_function():
    """
    Welcome function which salutes the user
    """
    title()
    print(
        "\033[0;34mWelcome to Battleship!\n"
        "Would you like to see the "
        "instructions or would you like to play already?"
    )

    ask_instructions = input(
        "Please type 1 for the instructions, "
        "2 if you wish to play!:\n"
    )

    while ask_instructions != "1" and ask_instructions != "2":
        ask_instructions = input(
            "\033[0;31mInvalid input, Please type 1 to "
            "see the instructions, or 2 to play "
            "the game:\n")

    if ask_instructions == "1":
        instructions()


def instructions():
    """
    Explains the game and let's the user play when
    he is ready
    """
    title()

    print(
        "\033[0;34mInstructions:\n"
        "You will first get asked to customize your game. "
        "You will input the size \nof the board "
        "and the number of ships you want per user.\n"
        "After that, you will choose the location "
        "of your boat. Each boat is 1 x 1. \n"
        "It's time to shoot! Once one of the players "
        "has no boats left,\nthe other player has won.\n"
        "If you both shoot the last boat of your opponent "
        "on the same round,\nit will be a draw. \n\n")

    # Ask user if they are ready to play.
    print("Are you ready to play?")
    ready = input("Please type 1 to continue:\n")
    # Make sure users input is valid.
    while ready != "1":
        ready = input(
            "\033[0;31mInvalid input, if you are ready "
            "press 1:\n"
        )


def input_board_size():
    """
    Inputs the user to choose the board size and
    returns the value as a list of two integers
    """
    title()
    board_size = []
    print("\033[0;34mChoose the size of the board.\n")
    while True:
        row = input("\033[0;34mPlease, choose number of rows (3 to 6):\n")
        if validate_board_size(row):
            board_size.append(int(row))
            break

    title()
    while True:
        col = input("\033[0;34mPlease, choose number of columns (3 to 6):\n")
        if validate_board_size(col):
            board_size.append(int(col))
            break
    title()
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
            raise ValueError()
    except ValueError:
        print(
            "\033[0;31mInvalid data: submit"
            " a value between 3 and 6, please try again.\n"
        )
        return False
    return True


def input_fleet_size():
    """
    Inputs user to specify the number of boats per board. (Between 3 and 8)
    """
    title()
    print("\033[0;34mChoose the number ships per user.\n")
    while True:
        boats = input("\033[0;34mPlease, choose between 3 to 8:\n")
        if validate_boat_fleet(boats):
            break
    title()
    return int(boats)


# Good idea to eliminate
def validate_boat_fleet(data):
    """
    Validates fleet size data by converting data into integer.
    Raises value error if value entered is not between 3 and 8.
    Also raises a value error if the value is not an integer.
    """
    try:
        check_data = int(data)
        if check_data >= 9 or check_data <= 2:
            raise ValueError()
    except ValueError:
        print(
            "\033[0;31mInvalid data: submit a value"
            " between 3 and 8, please try again.\n"
        )
        return False
    return True


class Board:
    """
    Class that creates the boards for the user and the enemy
    """
    def __init__(self, size, boats):
        self.size = size
        self.boats = boats
        self.board = [['\033[0;37m*' for x in range(size[1])]
                      for y in range(size[0])]
        self.guess = []
        self.miss = []
        self.boat_placement = []
        self.last_shot = 'No last shot'

    def user_print(self):
        """
        Prints the board in user friendly style.
        The location of the boats are visible.
        """
        for boat in self.boat_placement:
            self.board[boat[0]][boat[1]] = '\033[0;37m@'
        for guess in self.guess:
            self.board[guess[0]][guess[1]] = '\033[0;32mX'
        for miss in self.miss:
            self.board[miss[0]][miss[1]] = '\033[0;31m0'
        for row in self.board:
            print("\033[0;37m ".join(row))

    def enemy_print(self):
        """
        Prints the board without displaying the location of the boats
        that haven't been hit
        """
        for guess in self.guess:
            self.board[guess[0]][guess[1]] = '\033[0;32mX'
        for miss in self.miss:
            self.board[miss[0]][miss[1]] = '\033[0;31m0'
        for row in self.board:
            print("\033[0;37m ".join(row))

    def random_boat_selection(self):
        """
        Inputs a random boat selection used
        by the enemy
        """
        # Converting index user friendly to python friendly
        index1 = self.size[0] - 1
        index2 = self.size[1] - 1

        for boat in range(self.boats):
            while True:
                rand1 = random.randint(0, index1)
                rand2 = random.randint(0, index2)
                if self.validate_boat_placement(rand1, rand2):
                    break

    def manual_boat_placement(self):
        """
        Permits the user to select the location of the boats.
        User has to enter all the locations manually
        """
        title()
        print("\033[0;34mChoose the location of the boats.")
        print("Remember, you're grid is composed of: ")
        print(f"{self.size[0]} rows.")
        print(f"{self.size[1]} columns.\n")

        for boat in range(self.boats):
            while True:
                print(
                    "\033[0;34m"
                    f"Please, input boat nº {boat + 1} coordinates:\n"
                )
                while True:
                    row = input(
                        "\033[0;34m"
                        f"Row (Must be between 1 and {self.size[0]}):\n"
                    )
                    if self.validate_integer_input(row, self.size[0]):
                        if self.validate_range(int(row), self.size[0]):
                            break

                while True:
                    column = input(
                        "\033[0;34m"
                        f"Column(Must be between 1 and {self.size[1]}):\n"
                    )
                    if self.validate_integer_input(column, self.size[1]):
                        if self.validate_range(int(column), self.size[1]):
                            break

                if self.validate_boat_placement(int(row) - 1, int(column) - 1):
                    title()
                    print("\033[0;34m"f"Boat nº {boat + 1} placed!\n")
                    break
                else:
                    title()
                    print("\033[0;31mThere's already a boat in that location:")
                    print(
                        f"Row: {row}. "
                        f"Column: {column}.\n "
                    )

    def validate_integer_input(self, data, size):
        """
        Validates if the input is an intenger.
        Used multiple times throught the creation of the board:
        -Validation of the location of the boats
        -Validation of the shot during the game.
        """
        try:
            int(data)
        except ValueError:
            print(
                "\033[0;31mInvalid data:"
                f" submit a value between 1 and {size},"
                " please try again.\n"
            )
            return False
        return True

    def validate_range(self, data, size):
        """
        Validates if an integer is inside a range.
        Used multiple times throught the creation of the board:
        -Validation of the location of the boats
        -Validation of the shot during the game.
        """
        try:
            if size < data or data <= 0:
                raise ValueError()
        except ValueError:
            print(
                "\033[0;31mInvalid data:"
                f" submit a value between 1 and {size},"
                " please try again.\n")
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
        # If the column and row input are correct,
        # but the shot has already been made,
        # the while loop will resest from the begining
        while True:
            print("\033[0;34mLet's fire!")
            while True:
                row_shooting = input(
                    "\033[0;34m"
                    f"Choose a row between 1 and {self.size[0]}"
                    ": \n"
                )
                if self.validate_integer_input(row_shooting, self.size[0]):
                    row_shooting = int(row_shooting)
                    if self.validate_range(row_shooting, self.size[0]):
                        break

            while True:
                col_shooting = input(
                    "\033[0;34m"
                    f"Choose a column between 1 and {self.size[1]}"
                    ": \n"
                )
                if self.validate_integer_input(col_shooting, self.size[1]):
                    col_shooting = int(col_shooting)
                    if self.validate_range(col_shooting, self.size[1]):
                        break

            if self.validate_shots_taken(row_shooting - 1, col_shooting - 1):
                break
            else:
                print("\033[0;31mShot has already been made! Try again.\n")

    def automatic_shot_location(self):
        """
        Automatic shooting for the enemy
        """
        # Converting index user friendly to python friendly
        index1 = self.size[0] - 1
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
            self.last_shot = '\033[0;32mHIT!'
            self.guess.append([row, col])
            return True
        else:
            self.last_shot = "\033[0;31mMiss"
            self.miss.append([row, col])
            return True


def game_mechanics(fleet_size, user, enemy):
    """
    Game mechanics, checks if a player has won on the previous round.
    Displays the boards and the game section
    """
    while True:
        if len(enemy.guess) == fleet_size and len(user.guess) == fleet_size:
            draw_section()
            return False
        elif len(enemy.guess) == fleet_size:
            win_section()
            return False
        elif len(user.guess) == fleet_size:
            loose_section()
            return False
        else:
            # Displays the boards
            print("\033[0;34mUser board:")
            user.user_print()
            print("\033[0;34mEnemy board:")
            enemy.enemy_print()
            print("\n")
            print("\033[0;34m"f"Your last shot was: {enemy.last_shot}")
            print("\033[0;34m"f"Last enemy shot was: {user.last_shot}\n")
            # Stops the loop at this points, asking for location of next shot.
            enemy.input_shot_location()
            user.automatic_shot_location()
            title()


def play_again():
    """
    Permits user to play again or to exit the game after
    finishing
    """
    play = input(
        "\033[0;34mDo you wish to play again?"
        " If so press 1, if not press 2:\n"
    )
    while play != "1" and play != "2":
        play = input(
            "\033[0;31mInvalid input, Please type 1 to "
            "play again, or 2 to exit:\n")
    if play == "1":
        return False
    return True


def main():
    """
    Main function that calls all the other functions
    """
    initial_screen()
    while True:
        welcome_function()
        # Asks for inputs about the number of boats and size of the boards
        board_size = input_board_size()
        fleet_size = input_fleet_size()
        # Creates the boards for the enemy and the user
        user_board = Board(board_size, fleet_size)
        enemy_board = Board(board_size, fleet_size)
        # Add boats on the boards
        user_board.manual_boat_placement()
        enemy_board.random_boat_selection()
        title()
        # Game mechanics: stops the game when a player has won (or draw)
        game_mechanics(fleet_size, user_board, enemy_board)
        if play_again():
            break


main()
