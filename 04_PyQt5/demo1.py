from os import _exit
from sys import argv, exit
from time import sleep

from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
                             QLineEdit, QMessageBox, QPushButton, QRadioButton,
                             QWidget)


class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.Common()
    
    def Common(self):
        ## 屏幕中央 (app.desktop().width() - self.width()) // 2 , (app.desktop().height() - self.height()) // 2
        self.setGeometry(300, 50, 1000, 750)
        self.setWindowTitle('Demo')

        ## 不可放大
        self.setFixedSize(self.width(), self.height())

    def SignalFunc(self):
        pass


class UpdateData(QThread):
    signal = pyqtSignal()

    ## 带参数的信号 int, str, list, dict, 可复合在一起 pyqtSignal(int, str)
    ## signal2 = pyqtSignal(list)   signal2.emit([1,2,3])

    def run(self) -> None:
        while True:
            self.signal.emit()
            sleep(5.0)

if __name__ == '__main__':
    app = QApplication(argv)
    demo = Demo()
    demo.show()

    t = UpdateData()
    t.signal.connect(demo.SignalFunc)
    t.start()

    exit(app.exec_())