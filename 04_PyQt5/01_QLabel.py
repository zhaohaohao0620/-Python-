# -*- coding: utf-8 -*-

"""
    【简介】
        PyQT5中QLabel例子
        按住 Alt + N , Alt + P , Alt + O , Alt + C 切换组件控件
"""

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtWidgets import QTabWidget, QApplication, QLabel, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout


class TabDemo(QTabWidget):
    def __init__(self, parent=None):
        super(TabDemo, self).__init__(parent)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")
        self.tab1_ui()
        self.tab2_ui()
        self.setWindowTitle("QLabel")

    def tab1_ui(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        # 1
        label1.setText("这是一个文本标签。")
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.green)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>欢迎使用Python GUI 应用</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap("./../images/刘亦菲1.jpeg"))

        label4.setText("<A href='http://www.cnblogs.com/wangshuo1/'>欢迎访问信平的小屋</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是一个超链接标签')

        # 2
        vbox = QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addStretch()
        vbox.addWidget(label2)
        vbox.addStretch()
        vbox.addWidget(label3)
        vbox.addStretch()
        vbox.addWidget(label4)

        # 3
        # 打开允许访问超链接,默认是不允许，需要使用 setOpenExternalLinks(True)允许浏览器访问超链接
        label4.setOpenExternalLinks(True)
        # 点击文本框绑定槽事件
        label4.linkActivated.connect(link_clicked)

        # 划过文本框绑定槽事件
        label2.linkHovered.connect(link_hovered)
        label1.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.tab1.setLayout(vbox)

    def tab2_ui(self):
        name_lb1 = QLabel('&Name', self)
        name_ed1 = QLineEdit(self)
        name_lb1.setBuddy(name_ed1)

        name_lb2 = QLabel('&Password', self)
        name_ed2 = QLineEdit(self)
        name_lb2.setBuddy(name_ed2)

        btn_ok = QPushButton('&OK')
        btn_cancel = QPushButton('&Cancel')

        main_layout = QGridLayout(self)
        main_layout.addWidget(name_lb1, 0, 0)
        main_layout.addWidget(name_ed1, 0, 1, 1, 2)

        main_layout.addWidget(name_lb2, 1, 0)
        main_layout.addWidget(name_ed2, 1, 1, 1, 2)

        main_layout.addWidget(btn_ok, 2, 1)
        main_layout.addWidget(btn_cancel, 2, 2)

        self.tab2.setLayout(main_layout)


def link_hovered():
    print("当鼠标滑过label-2标签时，触发事件。")


def link_clicked():
    print("当鼠标点击label-4标签时，触发事件。")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = TabDemo()
    demo.show()
    sys.exit(app.exec_())
