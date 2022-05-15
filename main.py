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
        self.setStyleSheet("background-color: #3C013E;")

        self.header = QLabel("Simple Gaming",self)
        self.header.setStyleSheet("font: 20pt Showcard Gothic;" 
                            "color: gold;"
                            "font-weight: bold;")
        self.header.setGeometry(196, 10, 220, 100)

        self.tttbtn = QPushButton("Tic Tac Toe", self)
        self.tttbtn.setGeometry(60, 200, 220, 210)

        self.tttbtn.setStyleSheet("""
            QPushButton {
                border-image : url(./icons/ttt.png);
                font: 10pt Showcard Gothic;
                color: green;
                border-radius: 15px;
            }
            QPushButton:hover {
                color: yellow;
            }
        """)


        self.rpsbtn = QPushButton("Rock Paper Scissors", self)
        self.rpsbtn.setGeometry(300, 200, 220, 210)
        self.rpsbtn.setStyleSheet("""
            QPushButton {
                border-image : url(./icons/rps.jpg);
                font: 10pt Showcard Gothic;
                color: green;
                border-radius: 15px;
            }
            QPushButton:hover {
                color: yellow;
            }
        """)

        
        # Controller Instance
        self.Connect()
        self.control = Controller()

    def Connect(self):
        self.rpsbtn.clicked.connect(self.ShowRPS)
        self.tttbtn.clicked.connect(self.ShowTTT)

    def ShowTTT(self):
        self.control.TicTacToeWindow()
        # self.hide()

    def ShowRPS(self):
        self.control.RockPaperScissorsWindow()
        # self.hide()


app = QApplication(sys.argv)
# window.TicTacToeWindow()
main_window = App()
main_window.show()
app.exec()