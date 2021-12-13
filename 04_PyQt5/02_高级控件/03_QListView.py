import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListView, QMessageBox
from PyQt5.QtCore import QStringListModel


class ListViewDemo(QWidget):
    def __init__(self, parent=None):
        super(ListViewDemo, self).__init__(parent)
        # 设置初始大小与标题
        self.resize(300, 270)
        self.setWindowTitle('QListView 例子')



        # 实例化列表模型，添加数据
        slm = QStringListModel()
        self.qList = ['Item 1', 'Item 2', 'Item 3', 'Item 4']
        # 设置模型列表视图，加载数据列表
        slm.setStringList(self.qList)

        # 实例化列表视图
        listview = QListView()
        # 设置列表视图的模型
        listview.setModel(slm)

        # 单击触发自定义的槽函数
        listview.clicked.connect(self.clicked)

        # 设置窗口布局，加载控件
        layout = QVBoxLayout()

        layout.addWidget(listview)

        self.setLayout(layout)

    def clicked(self, model_index):
        # 提示信息弹窗，你选择的信息
        QMessageBox.information(self, 'ListWidget', '你选择了：' + self.qList[model_index.row()])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ListViewDemo()
    win.show()
    sys.exit(app.exec_())
