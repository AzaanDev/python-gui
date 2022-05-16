# Technical Spec

### RockPaperScissors Class
Creates the Rock Paper Scissors Game

init --> Creates a Window, Title, PlayerName Label, 
LineEdit for inputting name, Buttons for Player to choose from,
Text to display wins, Label to display CPU choice, A win counter LCD Widget

Some necessary functions include:

_Connect --> connects all the buttons to their actions

Select_Rock --> action for selecting rock
Select_Paper --> action for selecting paper
Select_Scissors --> action for selecting scissors

Cpu_Select --> randomly chooses rock, paper or scissors for CPU after player selects their choice

Check_Win --> Checks if the player has won the game, lost or draw 

Create_Back_Button --> creates a return to main window button, links the button to the action

Back_to --> the action of returning to main window

### Tic Tac Toe Class
Creates the Tic Tac Toe Game

Constructor - Creates all gui elements for the game (gridlayout of buttons, reset button, label for displaying the winner, QLCDNumber counter for win count and high score)

onClick() - Retrieves the last button clicked on by the user, updates the text to O, disables the buttons so it cannot be clicked again, checks if the user won, lost, or drew, increment the turns, and calls on the cpu to make a turn.

cpu() - Scans the array of buttons to find buttons that are still available, randomly chooses one from the list to change text to X and disabled it.

check_winner() - Checks every row, column, and diagonal for a winner. If user lost reset win_counter, if user won increment the win_counter and check for a new high score. Also, displays the win_view and disables all buttons.

disabledButtons() - Loops through the button List and disables all buttons

newHighScore() - Checks if the current win_counter > the high_score, updates the high_score and displays it, and saves the new high_score to the file.

Reset() - Clears all buttons text and enables them, sets turns to 0.

Back_t() - Closes the window

### Controller Class
Contains functions that create the TicTacToe and RockPaperScissor Windows

No constructor 

TicTacToeWindow()  - Creates TicTacToe Window and Shows it
RockPaperScissor() - Creates RockPaperScissor Window and shows it

### App Class 
Main Home Window, Displays options on game selection

Constructor - Creates the Window, sets window information (size and title), creates buttons and styles the window.

Connect() - Connects functions to buttons
ShowTTT() - Calls the Controllers's TicTacToeWindow() function
ShowRPS() - Calls the Controllers's RockPaperScissor() function

### Score Tracking Functions
Score File Strucute
0 - Rock Paper Scissor High Score
0 - Tic Tac Toe High Score

RockPaperScissor.py
save_score(val) - Takes a val can stores it into the first line in the file
load_score()    - Returns the value in the first line of the file

TicTacToe.py
save_score(val) - Takes a val can stores it into the second line in the file
load_score()    - Returns the value in the second line of the file
