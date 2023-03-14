from central_widget import CentralWidget
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Forgery Detection")

        central_widget = CentralWidget()

        self.setCentralWidget(central_widget)

app = QApplication(sys.argv)
window = Window()
window.showMaximized()
sys.exit(app.exec_())