# Tic-Tac-Toe Player vs AI

A Python-based Tic-Tac-Toe game where a player can play against an AI opponent. The AI uses a minimax algorithm to determine its move.

## Code Overview

### Functions

- `print_board(board)`: Displays the game board in the console.
- `check_winner(board, player)`: Checks if a player ('X' or 'O') has won.
- `get_moves(board)`: Returns a list of available moves on the board.
- `player_move(board)`: Handles player's move with error checking.
- `minimax(board, depth, is_maximizing)`: Recursively finds the best move for AI using the minimax algorithm.
- `ai_move(board)`: Determines and makes the AI's move.
- `main()`: Manages the main game loop and win/tie checks.

### Gameplay

- The player ('X') and AI ('O') take turns to make moves.
- The game board is displayed in the console, and the player is prompted to make a move by entering the row and column indices (0-2) separated by a space.
- The game continues until there is a winner or a tie.

## How to Play

1. Run the Python script in a suitable Python environment.
2. You will be prompted to enter your move in the format "row col".
3. The AI will make its move, and the updated board will be displayed.
4. The game continues until there is a winner or it's a tie.

### Valid Move Input

- Enter the row and column indices where you want to place your 'X', separated by a space. For example: `0 0`.
- Indices must be integers and within the range [0, 2].

## Additional Notes

- The AI uses a minimax algorithm, making it a perfect player that you cannot beat (at best, you can tie if you make no mistakes).
- The program does not employ a graphical UI, and it runs in the console.

## To-Do

- Implement a user-friendly graphical user interface (GUI).
- Add option to choose who goes first, the player or AI.
- Implement difficulty levels by adjusting the AI’s intelligence.

## Contribute

Feel free to fork, enhance, create issues, or submit pull requests. For major changes, kindly open an issue first to discuss proposed changes.

Enjoy playing!

## License
This project is licensed under the GNU General Public License v3.0 - see the LICENSE file for details.
