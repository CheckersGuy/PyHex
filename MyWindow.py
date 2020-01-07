import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import math


class MyWindow(QWidget):

    def start(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def __init__(self):
        super().__init__()
        self.title = "MyWindow"
        self.left = 50
        self.top = 50
        self.width = 640
        self.height = 480
        self.polygon = []
        self.polygon.append(self.createPolygon(50, 100, 100))
        self.polygon.append(self.createPolygon(50, 250, 100))
        self.show()

    def createPolygon(self, radius, off_x, off_y):
        polygon = QPolygonF()
        w = 360 / 6
        for i in range(6):
            angle = w * i + 60
            x = math.cos(math.radians(angle)) * radius + off_x
            y = math.sin(math.radians(angle)) * radius + off_y
            polygon.append(QPointF(x, y))
        return polygon

    def paintEvent(self, event):
        painter = QPainter(self)
        for poly in self.polygon:
            painter.drawPolygon(poly)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())
