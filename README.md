# Tic-Tac-Toe Game (Python)

Welcome to the Tic-Tac-Toe game! This is a simple command-line version of the classic game where you can play against a bot.

## Game Description
Tic-Tac-Toe is a two-player game, where one player is 'X' and the other is 'O'. In this version, you play as 'X', and the bot plays as 'O'. The game board is a 3x3 grid, and players take turns placing their marks in an empty spot on the grid. The first player to align three of their marks horizontally, vertically, or diagonally wins. If the grid is filled without a winner, the game ends in a tie.

## How to Play
1. The game will display the current state of the board.
2. You will be prompted to enter a number between 1 and 9 to place your 'X' on the grid (refer to the number system below).
3. The bot will then take its turn and place its 'O' on the grid.
4. The game will check for a winner after each turn. If there is a winner, the game will announce the result.
5. The game will end when there is a winner or the board is full (tie).

### Number System for Board
1 | 2 | 3  
--|---|--  
4 | 5 | 6  
--|---|--  
7 | 8 | 9  

### Example Gameplay:
```
Welcome to Tic Tac Toe  
Your turn (X):  
Please enter a number (1-9): 5  

Bot's turn (O):  
Bot chooses position 3  

You win!
```

## Requirements
- Python 3.x

## How to Run the Game
1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory where you saved the script.
4. Run the Python script with the following command:
   ```bash
   python tictactoe.py
   ```
5. Follow the on-screen prompts to play the game.

## Game Features
- A simple 3x3 Tic-Tac-Toe board.
- You play as 'X', and the bot plays as 'O'.
- The bot selects random valid moves.
- Game ends with a win or a tie.

## License
This project is open-source and available under the MIT License.

## Credits
- Created by Kavit Sheth.
```
