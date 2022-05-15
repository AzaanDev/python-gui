from PyQt5.QtWidgets import QPushButton, QLabel, QGridLayout, QWidget, QLCDNumber
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont
import random

class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic Tac Toe")
        self.setGeometry(600, 220, 800, 600)
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
        self.win_view = QLCDNumber(self)
        self.win_view.setGeometry(20, 50, 100, 50)
        self.win_view.move(10, 0)
        self.win_counter = 0
        self.turns = 0
        self.back = QPushButton("Return",self)
        self.back.clicked.connect(self.Back_to)


        self.layout.addWidget(self.resetButton, 4, 2)
        self.layout.addWidget(self.label, 4, 0)
        self.layout.addWidget(self.back, 4, 1)
        self.setLayout(self.layout)

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
                    self.win_counter = 0
                else:
                    self.label.setText("You Won")
                    self.win_counter += 1
                self.disableButtons()
                self.win_view.display(self.win_counter)
                return True

        for i in range(3):
            if self.button_list[(i, 0)].text() == self.button_list[(i, 1)].text() and self.button_list[(i, 0)].text() == self.button_list[(i, 2)].text() and self.button_list[(i, 0)].text() != "":
                if self.button_list[(i, 0)].text() == "X":
                    self.label.setText("You Lost")
                    self.win_counter = 0
                else:
                    self.label.setText("You Won")
                    self.win_counter += 1
                self.disableButtons()
                self.win_view.display(self.win_counter)
                return True

        if self.button_list[(0, 0)].text() == self.button_list[(1, 1)].text() and self.button_list[(0, 0)].text() == self.button_list[(2, 2)].text() and self.button_list[(0, 0)].text() != "":
            if self.button_list[(0, 0)].text() == "X":
                self.label.setText("You Lost")
                self.win_counter = 0
            else:
                self.label.setText("You Won")
                self.win_counter += 1
            self.disableButtons()
            self.win_view.display(self.win_counter)
            return True

        if self.button_list[(0, 2)].text() == self.button_list[(1, 1)].text() and self.button_list[(0, 2)].text() == self.button_list[(2, 0)].text() and self.button_list[(0, 2)].text() != "":
            if self.button_list[(0, 2)].text() == "X":
                self.label.setText("You Lost")
                self.win_counter = 0 
            else:
                self.label.setText("You Won")
                self.win_counter += 1
            self.disableButtons()
            self.win_view.display(self.win_counter)
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

    def Back_to(self):
        self.close()