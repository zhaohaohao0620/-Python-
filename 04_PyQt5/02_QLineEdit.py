# -*- coding: utf-8 -*-

"""
    【简介】
        PyQt5中 QLineEdit.EchoMode效果例子(密码)
        PyQt5中 QLineEdit的验证器例子(限制输入)
        PyQt5中 QLineEdit的输入掩码例子
        PyQt5中 QLineEdit综合例子
"""

import sys

from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QDoubleValidator, QRegExpValidator, QIntValidator, QFont
from PyQt5.QtWidgets import QTabWidget, QApplication, QWidget, QLineEdit, QFormLayout


def text_content_change(text):
    print("输入的内容为: " + text)


def enter_press():
    print("已输入值")


class Demo(QTabWidget):
    def __init__(self, parent=None):
        super(Demo, self).__init__(parent)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")
        self.addTab(self.tab3, "Tab 3")
        self.addTab(self.tab4, "Tab 4")
        self.tab1_ui()
        self.tab2_ui()
        self.tab3_ui()
        self.tab4_ui()
        self.setWindowTitle("QLineEdit")

    def tab1_ui(self):
        normal_line_edit = QLineEdit()
        no_echo_line_edit = QLineEdit()
        password_line_edit = QLineEdit()
        password_echo_on_edit_line_edit = QLineEdit()

        # 设置提示文本
        normal_line_edit.setPlaceholderText("Normal")
        no_echo_line_edit.setPlaceholderText("NoEcho")
        password_line_edit.setPlaceholderText("Password")
        password_echo_on_edit_line_edit.setPlaceholderText("PasswordEchoOnEdit")

        # 设置显示效果
        normal_line_edit.setEchoMode(QLineEdit.Normal)
        no_echo_line_edit.setEchoMode(QLineEdit.NoEcho)
        password_line_edit.setEchoMode(QLineEdit.Password)
        password_echo_on_edit_line_edit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        form_layout = QFormLayout()

        form_layout.addRow("Normal", normal_line_edit)
        form_layout.addRow("NoEcho", no_echo_line_edit)
        form_layout.addRow("Password", password_line_edit)
        form_layout.addRow("PasswordEchoOnEdit", password_echo_on_edit_line_edit)

        self.tab1.setLayout(form_layout)

    def tab2_ui(self):
        int_line_edit = QLineEdit()
        double_line_edit = QLineEdit()
        validator_line_edit = QLineEdit()

        int_line_edit.setPlaceholderText("整形")
        double_line_edit.setPlaceholderText("浮点型")
        validator_line_edit.setPlaceholderText("字母和数字")

        # 整形 范围：[1, 99]
        int_validator = QIntValidator(self)
        int_validator.setRange(1, 99)

        # 浮点型 范围：[-360, 360] 精度：小数点后2位
        double_validator = QDoubleValidator(self)
        double_validator.setRange(-360, 360)
        double_validator.setNotation(QDoubleValidator.StandardNotation)
        double_validator.setDecimals(2)

        # 字符和数字
        reg = QRegExp("[a-zA-Z0-9]+$")
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)

        # 设置验证器
        int_line_edit.setValidator(int_validator)
        double_line_edit.setValidator(double_validator)
        validator_line_edit.setValidator(validator)

        form_layout = QFormLayout()

        form_layout.addRow("整形", int_line_edit)
        form_layout.addRow("浮点型", double_line_edit)
        form_layout.addRow("字母和数字", validator_line_edit)

        self.tab2.setLayout(form_layout)

    def tab3_ui(self):
        ip_line_edit = QLineEdit()
        mac_line_edit = QLineEdit()
        date_line_edit = QLineEdit()
        license_line_edit = QLineEdit()

        ip_line_edit.setInputMask("000.000.000.000;_")
        mac_line_edit.setInputMask("HH:HH:HH:HH:HH:HH;_")
        date_line_edit.setInputMask("0000-00-00")
        license_line_edit.setInputMask('>AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#')

        form_layout = QFormLayout()

        form_layout.addRow("数字掩码", ip_line_edit)
        form_layout.addRow("Mac掩码", mac_line_edit)
        form_layout.addRow("日期掩码", date_line_edit)
        form_layout.addRow("许可证掩码", license_line_edit)

        self.tab3.setLayout(form_layout)

    def tab4_ui(self):
        e1 = QLineEdit()
        e1.setValidator(QIntValidator())
        e1.setMaxLength(4)
        e1.setAlignment(Qt.AlignRight)
        e1.setFont(QFont("Arial", 20))

        e2 = QLineEdit()
        e2.setValidator(QDoubleValidator(0.99, 99.99, 2))

        e3 = QLineEdit()
        e3.setInputMask('+99_9999_999999')

        e4 = QLineEdit()
        e4.textChanged.connect(text_content_change)

        e5 = QLineEdit()
        e5.setEchoMode(QLineEdit.Password)
        e5.editingFinished.connect(enter_press)

        e6 = QLineEdit("Hello PyQt5")
        e6.setReadOnly(True)

        form_layout = QFormLayout()

        form_layout.addRow("integer validator", e1)
        form_layout.addRow("Double validator", e2)
        form_layout.addRow("Input Mask", e3)
        form_layout.addRow("Text changed", e4)
        form_layout.addRow("Password", e5)
        form_layout.addRow("Read Only", e6)

        self.tab4.setLayout(form_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
