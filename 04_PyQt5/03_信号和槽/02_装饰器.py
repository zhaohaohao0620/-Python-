import sys
from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QPushButton
from PyQt5 import QtCore


# 发送者对象名称’就是使用setObjectName函数设置的名称，因此自定义槽函数的命名规则也可以看做：on+使用setObjectName设置的名称+信号名称
class CustWidget(QWidget):
    def __init__(self,parent=None):
        super(CustWidget, self).__init__(parent)

        #创建按钮，添加到自身窗口中
        self.okButton=QPushButton('ok',self)
        #使用setObjectName设置对象名称
        self.okButton.setObjectName('okButton')

        #设置自身的布局为水平布局，并添加按钮控件到其中
        layout=QHBoxLayout(self)
        layout.addWidget(self.okButton)


        #TODo 第一种方法
        #self.okButton.clicked.connect(self.okButton_clicked)

        #def okButton_clicked( self ):
        #   print('单击了ok按钮')

        #第二种方法
        QtCore.QMetaObject.connectSlotsByName(self)

    @QtCore.pyqtSlot()
    def on_okButton_clicked( self ):
        print('单击了ok按钮')


if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=CustWidget()
    win.show()
    sys.exit(app.exec_())