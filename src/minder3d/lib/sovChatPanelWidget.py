from PySide6.QtWidgets import QWidget

from .ui_sovChatPanelWidget import Ui_ChatPanelWidget


class ChatPanelWidget(QWidget, Ui_ChatPanelWidget):
    def __init__(self, gui, state, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state

        self.chatGoButton.clicked.connect(self.go)

    def go(self):
        """Print 'click'.

        This function prints 'click' to the console.

        Args:
            self: The instance of the class.
        """

        print('click')
