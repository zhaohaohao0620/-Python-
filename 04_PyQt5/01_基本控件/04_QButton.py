# -*- coding: utf-8 -*-

"""
    【简介】
        PyQt5中 QPushButton例子
        PyQt5中 QRadioButton例子
        PyQt5中 QCheckBoxButton例子
"""

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QTabWidget, QApplication, QWidget, QPushButton, QVBoxLayout, \
    QHBoxLayout, QRadioButton, QCheckBox, QGroupBox, QButtonGroup


class Demo(QTabWidget):
    def __init__(self, parent=None):
        super(Demo, self).__init__(parent)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")
        self.addTab(self.tab3, "Tab 3")
        self.tab1_ui()
        self.tab2_ui()
        self.tab3_ui()
        self.setWindowTitle("QButton")

    def tab1_ui(self):
        self.tab1_btn1 = QPushButton("Button1")
        self.tab1_btn1.setCheckable(True)
        self.tab1_btn1.toggle()
        self.tab1_btn1.clicked.connect(lambda: self.tab1_print_which_btn(self.tab1_btn1))
        self.tab1_btn1.clicked.connect(self.tab1_btn_state)

        self.tab1_btn2 = QPushButton('image')
        self.tab1_btn2.setIcon(QIcon(QPixmap("./../../images/python.png")))
        self.tab1_btn2.clicked.connect(lambda: self.tab1_print_which_btn(self.tab1_btn2))

        self.tab1_btn3 = QPushButton("Disabled")
        self.tab1_btn3.setEnabled(False)

        self.tab1_btn4 = QPushButton("&Download")
        self.tab1_btn4.setDefault(True)
        self.tab1_btn4.clicked.connect(lambda: self.tab1_print_which_btn(self.tab1_btn4))

        layout = QVBoxLayout()

        layout.addWidget(self.tab1_btn1)
        layout.addWidget(self.tab1_btn2)
        layout.addWidget(self.tab1_btn3)
        layout.addWidget(self.tab1_btn4)

        self.tab1.setLayout(layout)

    def tab2_ui(self):
        self.tab2_btn1 = QRadioButton("Button1")
        self.tab2_btn1.setChecked(True)
        self.tab2_btn1.toggled.connect(lambda: self.tab2_btn_state(self.tab2_btn1))

        self.tab2_btn2 = QRadioButton("Button2")
        self.tab2_btn2.toggled.connect(lambda: self.tab2_btn_state(self.tab2_btn2))

        self.tab2_btn3 = QRadioButton("Button3")
        self.tab2_btn4 = QRadioButton("Button4")

        bg1 = QButtonGroup(self)
        bg1.addButton(self.tab2_btn1, 1)
        bg1.addButton(self.tab2_btn2, 2)

        bg2 = QButtonGroup(self)
        bg2.addButton(self.tab2_btn3, 3)
        bg2.addButton(self.tab2_btn4, 4)

        layout = QVBoxLayout()

        layout1 = QHBoxLayout()
        layout2 = QHBoxLayout()

        layout1.addWidget(self.tab2_btn1)
        layout1.addWidget(self.tab2_btn2)
        layout2.addWidget(self.tab2_btn3)
        layout2.addWidget(self.tab2_btn4)

        layout.addLayout(layout1)
        layout.addLayout(layout2)

        self.tab2.setLayout(layout)

    def tab3_ui(self):
        group_box = QGroupBox("Checkboxes")
        group_box.setFlat(False)

        self.check_box1 = QCheckBox("&check_box1")
        self.check_box1.setChecked(True)
        self.check_box1.stateChanged.connect(lambda: self.tab3_btn3_tate())

        self.check_box2 = QCheckBox("check_box2")
        self.check_box2.toggled.connect(lambda: self.tab3_btn3_tate())

        self.check_box3 = QCheckBox("tristateBox")
        self.check_box3.setTristate(True)
        self.check_box3.setCheckState(Qt.PartiallyChecked)
        self.check_box3.stateChanged.connect(lambda: self.tab3_btn3_tate())

        layout = QHBoxLayout()
        layout.addWidget(self.check_box1)
        layout.addWidget(self.check_box2)
        layout.addWidget(self.check_box3)

        group_box.setLayout(layout)
        main_layout = QVBoxLayout()
        main_layout.addWidget(group_box)

        self.tab3.setLayout(main_layout)

    def tab1_btn_state(self):
        if self.tab1_btn1.isChecked():
            print("button pressed")
        else:
            print("button released")

    @staticmethod
    def tab1_print_which_btn(btn):
        print("clicked button is " + btn.text())

    @staticmethod
    def tab2_btn_state(btn):
        if btn.text() == "Button1":
            if btn.isChecked():
                print(btn.text() + " is selected")
            else:
                print(btn.text() + " is deselected")
        else:
            if btn.isChecked():
                print(btn.text() + " is selected")
            else:
                print(btn.text() + " is deselected")

    def tab3_btn3_tate(self):
        chk1_status = self.check_box1.text() + ", isChecked=" + str(self.check_box1.isChecked()) + ', chekState=' + str(
            self.check_box1.checkState()) + "\n"
        chk2_status = self.check_box2.text() + ", isChecked=" + str(
            self.check_box2.isChecked()) + ', checkState=' + str(
            self.check_box2.checkState()) + "\n"
        chk3_status = self.check_box3.text() + ", isChecked=" + str(
            self.check_box3.isChecked()) + ', checkState=' + str(
            self.check_box3.checkState()) + "\n"

        print(chk1_status + chk2_status + chk3_status)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
