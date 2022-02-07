# -*- coding: utf-8 -*-

"""
    【简介】
    PyQt5中 QSpinBox(计数器) 例子
"""

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QWidget, QApplication, QSpinBox


class Demo(QWidget):
    def __init__(self, parent=None):
        super(Demo, self).__init__(parent)
        self.setWindowTitle("SpinBox 例子")
        self.resize(300, 100)

        self.l1 = QLabel("current value:")
        self.l1.setAlignment(Qt.AlignCenter)
        self.sp = QSpinBox()
        self.sp.valueChanged.connect(self.value_change)

        layout = QVBoxLayout()

        layout.addWidget(self.l1)
        layout.addWidget(self.sp)

        self.setLayout(layout)

    def value_change(self):
        self.l1.setText("current value:" + str(self.sp.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
