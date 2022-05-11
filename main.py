from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock Paper Scissors")
        self.resize(QSize(600,600))

app = QApplication(sys.argv)
window = App()
window.show()
app.exec()
