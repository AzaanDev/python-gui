from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QFrame
from PyQt5.QtWidgets import QPushButton, QLineEdit
from PyQt5 import QtCore, Qt
from PyQt5.QtGui import QPixmap
import sys

class RockPaperScissors(QMainWindow):
    def __init__(self):
        super().__init__()
        # Window Creation
        self.setWindowTitle("Rock Paper Scissors")
        self.resize(QSize(600,600))
        # self.setStyleSheet("background: #036396;")

        # Title --- TODO: CENTER TITLE
        title = QLabel("Rock Paper Scissors", self)
        title.setGeometry(160, 10, 180, 100)
        title.setAlignment(QtCore.Qt.AlignCenter)
        title.setStyleSheet("font: 10pt Sans Serif;" 
                            "color: purple;"
                            "font-weight: bold;")

def main():
    app = QApplication(sys.argv)
    view = RockPaperScissors()
    view.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
