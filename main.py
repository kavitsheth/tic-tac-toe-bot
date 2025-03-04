import random


def print_board(x, z):
    print(
        f"{'X' if x[0] == 1 else 'O' if z[0] == 2 else '1'} | {'X' if x[1] == 1 else 'O' if z[1] == 2 else '2'} | {'X' if x[2] == 1 else 'O' if z[2] == 2 else '3'}")
    print(f"--|---|--")
    print(
        f"{'X' if x[3] == 1 else 'O' if z[3] == 2 else '4'} | {'X' if x[4] == 1 else 'O' if z[4] == 2 else '5'} | {'X' if x[5] == 1 else 'O' if z[5] == 2 else '6'}")
    print(f"--|---|--")
    print(
        f"{'X' if x[6] == 1 else 'O' if z[6] == 2 else '7'} | {'X' if x[7] == 1 else 'O' if z[7] == 2 else '8'} | {'X' if x[8] == 1 else 'O' if z[8] == 2 else '9'}")


def check_winner(state, player):
    # Check all win conditions for the player
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical
        (0, 4, 8), (2, 4, 6)  # diagonal
    ]
    for condition in win_conditions:
        if all(state[i] == player for i in condition):
            return True
    return False


def bot_move(x_state, z_state):
    # Find all available spots
    available_moves = [i for i in range(9) if x_state[i] == 0 and z_state[i] == 0]
    if available_moves:
        return random.choice(available_moves)
    return None


if __name__ == '__main__':
    x_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # X's moves
    z_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # O's moves
    game = True
    turn = 1  # 1 for X (user), 0 for O (bot)
    print("Welcome to Tic Tac Toe")

    while game:
        print_board(x_state, z_state)

        if turn == 1:  # User turn (X)
            print("Your turn (X):")
            value = int(input("Please enter a number (1-9): "))
            if value < 1 or value > 9 or (x_state[value - 1] != 0 or z_state[value - 1] != 0):
                print("Invalid move. Try again.")
                continue
            x_state[value - 1] = 1  # X's move
            turn = 0  # Switch turn to bot
        elif turn == 0:  # Bot's turn (O)
            print("Bot's turn (O):")
            move = bot_move(x_state, z_state)
            if move is not None:
                print(f"Bot chooses position {move + 1}")
                z_state[move] = 2  # Bot's move
                turn = 1  # Switch turn to player

        # Check for win condition for X (you)
        if check_winner(x_state, 1):
            print_board(x_state, z_state)
            print("You win!")
            game = False

        # Check for win condition for O (bot)
        elif check_winner(z_state, 2):
            print_board(x_state, z_state)
            print("Bot wins!")
            game = False

        # Check if the board is full (tie case)
        elif all(x_state[i] != 0 and z_state[i] != 0 for i in range(9)):
            print_board(x_state, z_state)
            print("It's a tie!")
            game = False