import sys
import cv2
import os
from PyQt5.QtCore import QUrl, QObject, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebChannel import QWebChannel


class WebBridge(QObject):
    def __init__(self, switch_callback):
        super().__init__()
        self.switch_callback = switch_callback

    @pyqtSlot()
    def goToCamera(self):
        self.switch_callback()


class WelcomePage(QWebEngineView):
    def __init__(self, switch_callback):
        super().__init__()
        self.bridge = WebBridge(switch_callback)
        self.channel = QWebChannel()
        self.channel.registerObject('bridge', self.bridge)
        self.page().setWebChannel(self.channel)

        path = os.path.abspath("pages/welcome.html")
        self.load(QUrl.fromLocalFile(path))


class CameraPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kamera")
        self.layout = QVBoxLayout()
        self.label = QLabel("Membuka Kamera...")
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

        self.cap = cv2.VideoCapture(0)
        self.timer_id = self.startTimer(30)

    def timerEvent(self, event):
        ret, frame = self.cap.read()
        if ret:
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb.shape
            img = QImage(rgb.data, w, h, ch * w, QImage.Format_RGB888)
            self.label.setPixmap(QPixmap.fromImage(img))

    def closeEvent(self, event):
        self.cap.release()
        super().closeEvent(event)


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplikasi Python Desktop")
        self.resize(800, 600)
        self.showWelcome()

    def showWelcome(self):
        self.welcome = WelcomePage(self.showCamera)
        self.setCentralWidget(self.welcome)

    def showCamera(self):
        self.camera = CameraPage()
        self.setCentralWidget(self.camera)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
