def welcome_function():
    """
    Welcome function which salutes the user
    """
    print("Welcome to this exciting match of the classic battleship game!")
    print("In this version, you will play against the machine, you will have the chance to choose how big you want your board and how many ships you would like.")
    

def input_board_size():
    """
    Inputs the user to choose the board size
    """
    print("Now you will choose the size of the board, it doesn't have to be a square, but rows and columns can be a maximun of 8 each.\n")
    print("Please, choose number of rows (1 to 8):") 
    rows = input()
    print("Please, choose number of columns (1 to 8):") 
    columns = input()

def validate_board_size(row, column):
    """
    Validates board size data by converting data into integer. 
    Raises value error if value entered is not between 1 and 8.
    Also raises a value error if the value is not an integer.
    """
    try:
        check_row = int(row)
        check_col = int(column)
        if check_row >= 9 and check_row <= 0:
            raise ValueError(
                f"Row value must be between 1 and 8, you provided {check_row}"
            )
        if check_col >= 9 and check_col <= 0:
            raise ValueError(
                f"Row value must be between 1 and 8, you provided {check_col}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

