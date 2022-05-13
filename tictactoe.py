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

    def onClick(self):
        button = self.sender()
        button.setText("O")
        button.setEnabled(False)
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

    def check_winner(self):
        
        return true