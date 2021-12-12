# -*- coding: utf-8 -*-

"""
    【简介】
        PyQT5中 QDialog 例子
        PyQT5中 QMessage 例子
        PyQT5中 QFontDialog 例子
        PyQT5中 QInputDialog 例子
"""

import sys

from PyQt5.QtCore import Qt, QDir
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QTabWidget, QApplication, QLabel, QWidget,
                             QVBoxLayout, QLineEdit, QPushButton, QDialog, QMessageBox, QFontDialog, QFormLayout,
                             QInputDialog, QFileDialog, QTextEdit)


class Demo(QTabWidget):
    def __init__(self, parent=None):
        super(Demo, self).__init__(parent)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")
        self.addTab(self.tab3, "Tab 3")
        self.addTab(self.tab4, "Tab 4")
        self.addTab(self.tab5, "Tab 5")
        self.tab1_ui()
        self.tab2_ui()
        self.tab3_ui()
        self.tab4_ui()
        self.tab5_ui()
        self.setWindowTitle("Dialog 例子")

    def tab1_ui(self):
        btn = QPushButton("弹出对话框", self.tab1)
        btn.clicked.connect(self.show_dialog)

        vbox = QVBoxLayout()

        vbox.addWidget(btn)

        self.tab1.setLayout(vbox)

    def tab2_ui(self):
        btn = QPushButton("弹出消息框", self.tab2)
        btn.clicked.connect(self.show_mes_dialog)

        vbox = QVBoxLayout()

        vbox.addWidget(btn)

        self.tab2.setLayout(vbox)

    def tab3_ui(self):
        btn = QPushButton("choose font", self.tab3)
        btn.clicked.connect(self.get_font)

        self.font_lineEdit = QLabel("Hello,测试字体例子", self.tab3)

        vbox = QVBoxLayout()

        vbox.addWidget(btn)
        vbox.addWidget(self.font_lineEdit)

        self.tab3.setLayout(vbox)

    def tab4_ui(self):
        btn1 = QPushButton("获得列表里的选项", self.tab4)
        btn1.clicked.connect(self.get_comboBox_item)
        self.le1 = QLineEdit()

        btn2 = QPushButton("获得字符串")
        btn2.clicked.connect(self.get_str_text)
        self.le2 = QLineEdit()

        btn3 = QPushButton("获得整数")
        btn3.clicked.connect(self.get_int_text)
        self.le3 = QLineEdit()

        layout = QFormLayout()

        layout.addRow(btn1, self.le1)
        layout.addRow(btn2, self.le2)
        layout.addRow(btn3, self.le3)

        self.tab4.setLayout(layout)

    def tab5_ui(self):
        btn = QPushButton("加载图片", self.tab5)
        btn.clicked.connect(self.get_file)
        self.tab5_le = QLabel("")

        btn1 = QPushButton("加载文本文件")
        btn1.clicked.connect(self.get_files)
        self.contents = QTextEdit()

        layout = QVBoxLayout()

        layout.addWidget(btn)
        layout.addWidget(self.tab5_le)
        layout.addWidget(btn1)
        layout.addWidget(self.contents)

        self.tab5.setLayout(layout)

    def show_dialog(self):
        dialog = QDialog()
        dialog.setWindowTitle("Dialog")
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()

    def show_mes_dialog(self):
        QMessageBox.information(self, "标题", "对话框消息正文", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    def get_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.font_lineEdit.setFont(font)

    def get_comboBox_item(self):
        items = ("C", "C++", "Java", "Python")
        item, ok = QInputDialog.getItem(self, "select input dialog",
                                        "语言列表", items, 0, False)
        if ok and item:
            self.le1.setText(item)

    def get_str_text(self):
        text, ok = QInputDialog.getText(self, 'Text Input dialog', '输入姓名:')
        if ok:
            self.le2.setText(str(text))

    def get_int_text(self):
        num, ok = QInputDialog.getInt(self, "integer input dialog", "输入数字")
        if ok:
            self.le3.setText(str(num))

    def get_file(self):
        f_name, _ = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Image files (*.jpg *.gif)")
        self.tab5_le.setPixmap(QPixmap(f_name))

        QFileDialog.getOpenFileNames(self, "多文件选择", "./", "All Files (*);;Text Files (*.txt)")

        QFileDialog.getExistingDirectory(self, "选取文件夹", "./")

    def get_files(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter(QDir.Files)

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            f = open(filenames[0], 'r')

            with f:
                data = f.read()
                self.contents.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
