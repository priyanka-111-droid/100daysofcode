import random

# Initialize the Tic Tac Toe grid as a list of lists (2D array)
grid = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
]

# Function to print the current state of the Tic Tac Toe grid
def print_grid():
    for row in grid:
        print(" ".join(row))
    print()

# Function to check if a player has won horizontally
def row_win(grid, symbol):
    for row in grid:
        if all(cell == symbol for cell in row):
            return True
    return False

# Function to check if a player has won vertically
def col_win(grid, symbol):
    for col in range(len(grid[0])):
        if all(grid[row][col] == symbol for row in range(len(grid))):
            return True
    return False

# Function to check if a player has won diagonally
def diag_win(grid, symbol):
    if all(grid[i][i] == symbol for i in range(len(grid))) or all(grid[i][len(grid) - 1 - i] == symbol for i in range(len(grid))):
        return True
    return False

# Function to check if the game is a tie
def is_tie(grid):
    return all(cell != '_' for row in grid for cell in row)


# Main game 
def game():
    while True:
        # User's turn
        user_posx, user_posy = [int(x) for x in input("Enter row number and column number (follow 1-based indexing): ").split()]
        if grid[user_posx - 1][user_posy - 1] == '_':
            grid[user_posx - 1][user_posy - 1] = 'X'
        else:
            print("Cell already occupied. Try again.")
            continue

        print_grid()

        # Check if the user has won
        if row_win(grid, 'X') or col_win(grid, 'X') or diag_win(grid, 'X'):
            print("Congratulations! You win!")
            break

        # Check for a tie
        if is_tie(grid):
            print("It's a tie!")
            break

        # Computer's turn
        while True:
            computer_posx, computer_posy = random.randint(1, 3), random.randint(1, 3)
            if grid[computer_posx - 1][computer_posy - 1] == '_':
                grid[computer_posx - 1][computer_posy - 1] = 'O'
                break

        print_grid()

        # Check if the computer has won
        if row_win(grid, 'O') or col_win(grid, 'O') or diag_win(grid, 'O'):
            print("Computer wins!")
            break

        # Check for a tie
        if is_tie(grid):
            print("It's a tie!")
            break



def welcome():
    print(
    '''
    WELCOME TO TIC-TAC-TOE!!!!!!
    Your symbol is "X" and you will be fighting against the computer whose symbol is "O".
    '''
    )
    game()


if __name__=='__main__':
    welcome()

