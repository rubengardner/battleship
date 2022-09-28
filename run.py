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
    board_size = []
    print("Now you will choose the size of the board, it doesn't have to be a square, but rows and columns can be a maximun of 8 each.\n")
    while True:
        print("Please, choose number of rows (1 to 8):") 
        row = input()
        if validate_board_size(row):
            board_size.append(int(row))
            break

    while True:
        print("Please, choose number of columns (1 to 8):") 
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
        if check_data >= 9 or check_data <= 0:
            raise ValueError(
                f"Value must be between 1 and 8, you provided {check_data}"
            )
        
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True

class board:
  def __init__(self, name, rows, columns):
    self.name = name
    self.rows = rows
    self.columns = columns


def main():
    welcome_function()
    input_board_size()


main()
