# -*- coding: utf-8 -*-

"""
    【简介】
    PyQt5中 QComboBox(下拉框) 例子
"""

import sys

from PyQt5.QtWidgets import QVBoxLayout, QLabel, QComboBox, QWidget, QApplication


class Demo(QWidget):
    def __init__(self, parent=None):
        super(Demo, self).__init__(parent)
        self.setWindowTitle("QComboBox 例子")
        self.lbl = QLabel("")

        self.cb = QComboBox()
        self.cb.addItem("C")
        self.cb.addItem("C++")
        self.cb.addItems(["Java", "C#", "Python"])
        self.cb.currentIndexChanged.connect(self.selection_change)
        self.cb.activated.connect(self.test1)
        self.cb.highlighted.connect(self.test2)

        layout = QVBoxLayout()

        layout.addWidget(self.cb)
        layout.addWidget(self.lbl)
        self.setLayout(layout)

    def selection_change(self, i):
        self.lbl.setText(self.cb.currentText())
        self.lbl.adjustSize()

        print("Items in the list are :")
        for count in range(self.cb.count()):
            print('item' + str(count) + '=' + self.cb.itemText(count))
            print("Current index", i, "selection changed ", self.cb.currentText())

    def test1(self):
        print("1")

    def test2(self):
        print("2")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
