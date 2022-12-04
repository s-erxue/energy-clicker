from typing import Optional

from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout

from src import State


class ClickPanel(QWidget):
    state: State
    energy_listener_id: int

    text: QLabel

    def __init__(self, state: State, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        self.state = state

        self.text = QLabel('0')
        self.text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        button = QPushButton('Click')
        button.clicked.connect(self.increment)

        box = QVBoxLayout(self)
        box.addWidget(self.text)
        box.addWidget(button)

        self.energy_listener_id = self.state.register_energy_listener(lambda energy: self.text.setText(str(energy)))

    @Slot()
    def increment(self):
        self.state.energy += 1

    def destroy(self, destroyWindow: bool = True, destroySubWindows: bool = True) -> None:
        self.state.unregister_energy_listener(self.energy_listener_id)

        super().destroy(destroyWindow, destroySubWindows)
