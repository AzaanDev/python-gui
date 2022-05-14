from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedLayout, QStackedWidget, QWidget, QPushButton, QLabel
from PyQt5.QtCore import QSize
from tictactoe import TicTacToe
import sys


class Controller:
    def __init__(self):
     pass
    
    def TicTacToeWindow(self):
        self.window = TicTacToe()
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

        self.rspbtn = QPushButton("Rock Paper Scissors", self)
        self.rspbtn.setGeometry(300, 200, 220, 210)

    def Connect(self):

    def MakeTTTInstance(self):

    def MakeRSPInstance(self):
        


app = QApplication(sys.argv)
# window = Controller()
# window.TicTacToeWindow()
main_window = App()
main_window.show()
app.exec()
