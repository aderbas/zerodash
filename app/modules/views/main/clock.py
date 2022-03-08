"""Clock component."""
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, QTime, Qt

class MainClock(QVBoxLayout):
    """Main class for clock component."""

    def __init__(self, window: QWidget):
        super().__init__()

        font = QFont('Arial', 80, QFont.Bold)

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignHCenter)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #CCCCCC;")

        # adding label to the layout
        self.addWidget(self.label)

        # creating a timer object
        timer = QTimer(window)
        timer.timeout.connect(self.show_time)
        timer.start(1000)

    def show_time(self):
        """Called by timer."""

        # getting current time
        current_time = QTime.currentTime()

        # converting QTime object to string
        label_time = current_time.toString('hh:mm:ss')

        # showing it to the label
        self.label.setText(label_time)
       