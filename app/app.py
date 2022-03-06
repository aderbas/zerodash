"""Main application file."""
import sys
from PyQt5.QtWidgets import QApplication
from app.modules.views.main import MainWindow

def create_app():
    """Create pyqt5 application."""
    app = QApplication(sys.argv)

    # create the instance of our Window
    window = MainWindow()

    # showing all the widgets
    window.show()

    # start the app
    app.exit(app.exec_())
