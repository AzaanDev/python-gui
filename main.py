from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedLayout, QStackedWidget, QWidget, QPushButton, QLabel
from PyQt5.QtCore import QSize
from RockPaperScissors import RockPaperScissors
from tictactoe import TicTacToe
import sys


class Controller:
    def __init__(self):
     pass
    
    def TicTacToeWindow(self):
        self.window = TicTacToe()
        self.window.show()

    def RockPaperScissorsWindow(self):
        self.window = RockPaperScissors()
        self.window.show()



class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Gaming")
        self.resize(QSize(600,600))

        self.header = QLabel("Game App",self)
        self.header.setStyleSheet("font: 10pt Sans Serif;" 
                            "color: purple;"
                            "font-weight: bold;")
        self.header.setGeometry(210, 10, 180, 100)

        self.tttbtn = QPushButton("Tic Tac Toe", self)
        self.tttbtn.setGeometry(60, 200, 220, 210)

        self.rpsbtn = QPushButton("Rock Paper Scissors", self)
        self.rpsbtn.setGeometry(300, 200, 220, 210)

        # Controller Instance
        self.control = Controller()

    def Connect(self):
        self.rpsbtn.clicked.connect(self.ShowRPS)
        self.tttbtn.clicked.connect(self.ShowTTT)

    def ShowTTT(self):
        self.control.TicTacToeWindow()

    def ShowRPS(self):
        self.control.RockPaperScissorsWindow()
        


app = QApplication(sys.argv)
# window.TicTacToeWindow()
main_window = App()
main_window.show()
app.exec()
