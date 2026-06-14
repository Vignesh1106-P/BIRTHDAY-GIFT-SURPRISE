import sys
import os

# Hide console
if sys.platform == 'win32':
    import ctypes
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon

class BirthdayApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Birthday Surprise 🎂")
        self.setMinimumSize(1400, 900)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://birthday-gift-surprise-production.up.railway.app/login/"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BirthdayApp()
    window.show()
    sys.exit(app.exec_())