from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedLayout, QStackedWidget, QWidget, QPushButton
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
        self.setWindowTitle("Temp Name")
        self.resize(QSize(600,600))
        


app = QApplication(sys.argv)
window = Controller()
window.TicTacToeWindow()
app.exec()