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

        # Title
        title = QLabel("Rock Paper Scissors", self)
        title.setGeometry(210, 10, 180, 100)
        title.setAlignment(QtCore.Qt.AlignCenter)
        title.setStyleSheet("font: 10pt Sans Serif;" 
                            "color: purple;"
                            "font-weight: bold;")

        self._PlayerName()
        self._GameButtons()

    def _PlayerName(self):

        # QLabel for player name
        playername = QLabel("Player Name: ", self)
        playername.setAlignment(QtCore.Qt.AlignCenter)
        playername.setGeometry(5,170,100,100)
        playername.setStyleSheet("font: 10pt Sans Serif;" 
                            "color: blue;"
                            "font-weight: bold;")

        # QLineEdit
        inputname = QLineEdit(self)
        inputname.setGeometry(110,212,120,18)

    def _GameButtons(self):
        # Layout 

        # Buttons
        rbtn = QPushButton(self)
        rbtn.setGeometry(10,240,70,70)
        rbtn.setStyleSheet("border-image : url(python-gui/icons/rock.jpg);")

        pbtn = QPushButton(self)
        pbtn.setGeometry(90,240,70,70)
        pbtn.setStyleSheet("border-image : url(python-gui/icons/paper.jpg);")


        sbtn = QPushButton(self)
        sbtn.setGeometry(170,240,70,70)
        sbtn.setStyleSheet("border-image : url(python-gui/icons/scissors.jpg);")
        # b3.setStyleSheet("Background-color: Green")

        # VS label
        vs = QLabel("vs.", self)
        vs.setAlignment(QtCore.Qt.AlignCenter)
        vs.setGeometry(250,240,70,70)
        vs.setStyleSheet("font: 10pt Sans Serif;" 
                            "color: red;"
                            "font-weight: bold;")

        # CPU Label
        cpu_choice = QLabel("Default", self)
        cpu_choice.setGeometry(350, 200, 130, 150)
        pixmap = QPixmap('C:/Users/Danie/Desktop/githubProjects/python-gui/icons/paper.jpg').scaled(130,150)
        cpu_choice.setPixmap(pixmap)

def main():
    app = QApplication(sys.argv)
    view = RockPaperScissors()
    view.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
