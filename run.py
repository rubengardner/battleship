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
    print("Now you will choose the size of the board, it doesn't have to be a square, but rows and columns can be a maximun of 8 each/n")
    print("Please, choose number of rows (1 to 8):") 
    rows = input()
    print("Please, choose number of columns (1 to 8):") 
    columns = input()
