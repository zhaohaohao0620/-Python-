import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction


class ToolBarDemo(QMainWindow):
    def __init__(self, parent=None):
        super(ToolBarDemo, self).__init__(parent)
        # 设置标题与初始大小
        self.setWindowTitle('toolbar例子')
        self.resize(300, 200)

        # 在工具栏区域添加文件工具栏
        tb = self.addToolBar('File')
        # 添加图形按钮
        new = QAction(QIcon('./../../../images/new.png'), 'new', self)
        _open = QAction(QIcon('./../../images/open.png'), 'open', self)
        save = QAction(QIcon('./../../images/save.png'), 'save', self)

        tb.addAction(new)
        tb.addAction(_open)
        tb.addAction(save)

        # 图形对象点击触发自定义槽函数
        tb.actionTriggered[QAction].connect(self.tool_btn_pressed)

    def tool_btn_pressed(self, a):
        # 输出，点击地图性按钮
        print('pressed tool button is ', a.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = ToolBarDemo()
    demo.show()
    sys.exit(app.exec_())
