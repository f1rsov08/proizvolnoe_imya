import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class Suprematism(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.qp = QPainter()
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.make_ball()
        self.update()

    def make_ball(self):
        self.bx = randint(0, self.size().width() - 300 if self.size().width() >= 300 else 0)
        self.by = randint(0, self.size().height() - 300 if self.size().height() >= 300 else 0)
        self.bs = randint(0, min(self.size().width(), self.size().height()))

    def draw(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(self.bx * (self.bx > 0), self.by * (self.by > 0), self.bs, self.bs)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())
