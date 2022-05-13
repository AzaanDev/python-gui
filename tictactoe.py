from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QGridLayout, QWidget
from PyQt5.QtCore import QSize
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
                self.button_list[(i, j)].clicked.connect(self.onClick)
                self.layout.addWidget(self.button_list[(i, j)], i, j)
        self.setLayout(self.layout)
        self.turns = 0

    def onClick(self):
        self.turns += 1
        button = self.sender()
        button.setText("O")
        button.setEnabled(False)
        if not self.check_winner():
            if self.turns == 9:
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
                    pass
                else:
                    pass
                self.disableButtons()
                return True

        for i in range(3):
            if self.button_list[(i, 0)].text() == self.button_list[(i, 1)].text() and self.button_list[(i, 0)].text() == self.button_list[(i, 2)].text() and self.button_list[(i, 0)].text() != "":
                if self.button_list[(i, 0)].text() == "X":
                    pass 
                else:
                    pass
                self.disableButtons()
                return True

        if self.button_list[(0, 0)].text() == self.button_list[(1, 1)].text() and self.button_list[(0, 0)].text() == self.button_list[(2, 2)].text() and self.button_list[(0, 0)].text() != "":
            if self.button_list[(0, 0)].text() == "X":
                pass 
            else:
                pass
            self.disableButtons()
            return True

        if self.button_list[(0, 2)].text() == self.button_list[(1, 1)].text() and self.button_list[(0, 2)].text() == self.button_list[(2, 0)].text() and self.button_list[(0, 2)].text() != "":
            if self.button_list[(0, 2)].text() == "X":
                pass 
            else:
                pass
            self.disableButtons()
            return True

        return False

    def disableButtons(self):
        for i in range(3): 
           for j in range(3): 
                self.button_list[(i, j)].setEnabled(False)