"""
    【简介】
    PyQt5中 QPixmap 例子

"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QpixmapDemo(QWidget):
    def __init__(self, parent=None):
        super(QpixmapDemo, self).__init__(parent)
        self.setWindowTitle('QPixmap例子')

        layout = QVBoxLayout()

        lab1 = QLabel()
        lab1.setPixmap(QPixmap('./../../images/python.png'))

        layout.addWidget(lab1)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = QpixmapDemo()
    demo.show()
    sys.exit(app.exec_())
