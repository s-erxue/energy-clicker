from sys import argv

from PySide6.QtWidgets import QApplication

from src import State
from src.widgets import ClickPanel

if __name__ == '__main__':
    state = State()

    app = QApplication(argv)
    label = ClickPanel(state)
    label.resize(1024, 768)
    label.setWindowTitle("Energy Clicker")
    label.show()
    app.exec()
