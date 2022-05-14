from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLCDNumber
from PyQt5 import QtCore, Qt
from PyQt5.QtGui import QPixmap
import sys
import random

class RockPaperScissors(QWidget):
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

        # Player Name
        self.playername = QLabel("Player Name: ", self)
        self.playername.setAlignment(QtCore.Qt.AlignCenter)
        self.playername.setGeometry(5,170,100,100)
        self.playername.setStyleSheet("font: 10pt Sans Serif;" 
                            "color: blue;"
                            "font-weight: bold;")
        # QLineEdit
        self.inputname = QLineEdit(self)
        self.inputname.setGeometry(110,212,120,18)

        # Buttons
        self.rbtn = QPushButton(self)
        self.rbtn.setGeometry(10,240,70,70)
        self.rbtn.setStyleSheet("border-image : url(python-gui/icons/rock.jpg);")

        self.pbtn = QPushButton(self)
        self.pbtn.setGeometry(90,240,70,70)
        self.pbtn.setStyleSheet("border-image : url(python-gui/icons/paper.jpg);")


        self.sbtn = QPushButton(self)
        self.sbtn.setGeometry(170,240,70,70)
        self.sbtn.setStyleSheet("border-image : url(python-gui/icons/scissors.jpg);")
        # b3.setStyleSheet("Background-color: Green")

        # VS label
        self.vs = QLabel("vs.", self)
        self.vs.setAlignment(QtCore.Qt.AlignCenter)
        self.vs.setGeometry(250,240,70,70)
        self.vs.setStyleSheet("font: 10pt Sans Serif;" 
                            "color: red;"
                            "font-weight: bold;")

        # Connections
        self._Connect()

        # CPU
        self.cpu_choice = QLabel("Default", self)
        self.cpu_choice.setGeometry(350, 200, 130, 150)
        pixmap = QPixmap('C:/Users/Danie/Documents/AdvPycharm/guistuff/project/icons/question.png').scaled(130,150)
        self.cpu_choice.setPixmap(pixmap)

        # Text for Win
        self.win = QLabel("Who will win?", self)
        self.win.setGeometry(200, 300, 200, 300)
        self.win.setStyleSheet("font: 14pt Sans Serif;" 
                    "color: blue;"
                    "font-weight: bold;")
        # self.win.setAlignment(QtCore.Qt.AlignCenter)

        # Win Counter var
        self.win_counter = 0

        # Win Counter LCD view
        self.win_view = QLCDNumber(self)
        self.win_view.setGeometry(20, 50, 150, 71)


    def _Connect(self):
        # Connect
        self.rbtn.clicked.connect(self.Select_Rock)
        self.pbtn.clicked.connect(self.Select_Paper)
        self.sbtn.clicked.connect(self.Select_Scissors)

    def Select_Rock(self):
        self.player_select = 1

        self.Cpu_Select()
        self.Check_Win()
    
    def Select_Paper(self):
        self.player_select = 2

        self.Cpu_Select()
        self.Check_Win()

    def Select_Scissors(self):
        self.player_select = 3

        self.Cpu_Select()
        self.Check_Win()

    # CPU Label

    # CPU SELECTION
    def Cpu_Select(self):
        self.cpu_select = random.randint(1,3)

        if self.cpu_select == 1:
            pixmap = QPixmap('C:/Users/Danie/Documents/AdvPycharm/guistuff/project/icons/rock.jpg').scaled(130,150)
            self.cpu_choice.setPixmap(pixmap)
        elif self.cpu_select == 2:
            pixmap = QPixmap('C:/Users/Danie/Documents/AdvPycharm/guistuff/project/icons/paper.jpg').scaled(130,150)
            self.cpu_choice.setPixmap(pixmap)
        elif self.cpu_select == 3:
            pixmap = QPixmap('C:/Users/Danie/Documents/AdvPycharm/guistuff/project/icons/scissors.jpg').scaled(130,150)
            self.cpu_choice.setPixmap(pixmap)

    def Check_Win(self):
        #Draw
        if self.player_select == self.cpu_select:
            self.win.setText("Draw")
            return
        
        if self.player_select == 1: # Player selected Rock
            if self.cpu_select == 3:
                self.win.setText("You win!")
                self.win_counter += 1
                self.win_view.display(self.win_counter)

            else:
                self.win.setText("You Lose.")
                self.win_counter = 0
                self.win_view.display(self.win_counter)

        elif self.player_select == 2: # Player selected Rock
            if self.cpu_select == 1:
                self.win.setText("You win!")
                self.win_counter += 1
                self.win_view.display(self.win_counter)

            else:
                self.win.setText("You Lose.")
                self.win_counter = 0
                self.win_view.display(self.win_counter)

        elif self.player_select == 3: # Player selected Rock
            if self.cpu_select == 2:
                self.win.setText("You win!")
                self.win_counter += 1
                self.win_view.display(self.win_counter)

            else:
                self.win.setText("You Lose.")
                self.win_counter = 0
                self.win_view.display(self.win_counter)


def main():
    app = QApplication(sys.argv)
    view = RockPaperScissors()
    view.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()