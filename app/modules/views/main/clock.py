"""Clock component."""
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, QTime, Qt

class MainClock(QVBoxLayout):
    """Main class for clock component."""

    def __init__(self, window: QWidget):
        super().__init__()

        # creating font object
        font = QFont('Arial', 80, QFont.Bold)

        # creating a label object
        self.label = QLabel()

        # setting centre alignment to the label
        self.label.setAlignment(Qt.AlignCenter)

        # setting font to the label
        self.label.setFont(font)

        # setting font color
        self.label.setStyleSheet("color: #CCCCCC;")

        # adding label to the layout
        self.addWidget(self.label)

        # creating a timer object
        timer = QTimer(window)

        # adding action to timer
        timer.timeout.connect(self.show_time)

        # update the timer every second
        timer.start(1000)

    def show_time(self):
        """Called by timer."""

        # getting current time
        current_time = QTime.currentTime()

        # converting QTime object to string
        label_time = current_time.toString('hh:mm:ss')

        # showing it to the label
        self.label.setText(label_time)
       