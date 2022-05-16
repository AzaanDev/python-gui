from PyQt5.QtWidgets import QPushButton, QLabel, QGridLayout, QWidget
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont
import random

class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic Tac Toe")
        self.setGeometry(400, 200, 800, 600)
        self.layout = QGridLayout()
        self.button_list = {}
        for i in range(3): 
           for j in range(3): 
                self.button_list[(i, j)] = QPushButton()
                self.button_list[(i, j)].setMinimumHeight(100)
                self.button_list[(i, j)].setFont(QFont("Times", 50, QFont.Bold))
                self.button_list[(i, j)].clicked.connect(self.onClick)
                self.layout.addWidget(self.button_list[(i, j)], i, j)

        self.resetButton = QPushButton("Reset", self)
        self.resetButton.clicked.connect(self.Reset)
        self.label = QLabel('Your Turn', self)
        self.label.setAlignment(Qt.AlignCenter)
        
        self.layout.addWidget(self.resetButton, 4, 2)
        self.layout.addWidget(self.label, 4, 0)
        self.setLayout(self.layout)
        self.turns = 0

    def onClick(self):
        self.turns += 1
        button = self.sender()
        button.setText("O")
        button.setEnabled(False)
        if not self.check_winner():
            if self.turns == 9:
                self.label.setText("Draw")
                return
            self.turns += 1
            self.cpu()

    def cpu(self):
        available_moves = []
        for i in range(3): 
           for j in range(3): 
                if self.button_list[(i, j)].isEnabled():
                    available_moves.append((i, j))
        move = random.choice(available_moves)
        self.button_list[move].setText("X")
        self.button_list[move].setEnabled(False)
        self.check_winner()

    def check_winner(self):
        for i in range(3):
            if self.button_list[(0, i)].text() == self.button_list[(1, i)].text() and self.button_list[(0, i)].text() == self.button_list[(2, i)].text() and self.button_list[(0, i)].text() != "":
                if self.button_list[(0, i)].text() == "X":
                    self.label.setText("You Lost")
                else:
                    self.label.setText("You Won")
                self.disableButtons()
                return True

        for i in range(3):
            if self.button_list[(i, 0)].text() == self.button_list[(i, 1)].text() and self.button_list[(i, 0)].text() == self.button_list[(i, 2)].text() and self.button_list[(i, 0)].text() != "":
                if self.button_list[(i, 0)].text() == "X":
                    self.label.setText("You Lost") 
                else:
                    self.label.setText("You Won")
                self.disableButtons()
                return True

        if self.button_list[(0, 0)].text() == self.button_list[(1, 1)].text() and self.button_list[(0, 0)].text() == self.button_list[(2, 2)].text() and self.button_list[(0, 0)].text() != "":
            if self.button_list[(0, 0)].text() == "X":
                self.label.setText("You Lost")
            else:
                self.label.setText("You Won")
            self.disableButtons()
            return True

        if self.button_list[(0, 2)].text() == self.button_list[(1, 1)].text() and self.button_list[(0, 2)].text() == self.button_list[(2, 0)].text() and self.button_list[(0, 2)].text() != "":
            if self.button_list[(0, 2)].text() == "X":
                self.label.setText("You Lost") 
            else:
                self.label.setText("You Won")
            self.disableButtons()
            return True

        return False


    def disableButtons(self):
        for i in range(3): 
           for j in range(3): 
                self.button_list[(i, j)].setEnabled(False)

    def Reset(self):
        for i in range(3): 
           for j in range(3): 
                self.button_list[(i, j)].setText('')
                self.button_list[(i, j)].setEnabled(True)
        self.turns = 0
        self.label.setText("Your Turn")

def save_score(val): #TTT save
    s = str(val)
    f = open("score.txt","r+")
    l = f.readlines()
    l[1] = s
    p = l[0] + l[1]
    f.seek(0)
    f.write(p)
    f.truncate()
        
def load_score(): #TTT load
    f = open("score.txt","r+")
    l = f.readlines()
    return l[1] 