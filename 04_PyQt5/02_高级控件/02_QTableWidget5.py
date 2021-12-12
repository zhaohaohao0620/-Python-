import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QHeaderView, QTableWidgetItem, QTableWidget, QApplication, QMenu, QWidget


class Table(QWidget):
    def __init__(self):
        super(Table, self).__init__()
        self.initUI()

    def initUI(self):
        # 设置标题与初始大小
        self.setWindowTitle('QTableWidget demo')
        self.resize(500, 300)

        self.tableWidget = QTableWidget(5, 3)

        # 设置表格水平方向的头标签
        self.tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重'])

        # 设置水平方向自动伸缩填满窗口
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 添加数据到指定行列
        newItem = QTableWidgetItem("张三")
        self.tableWidget.setItem(0, 0, newItem)

        newItem = QTableWidgetItem("男")
        self.tableWidget.setItem(0, 1, newItem)

        newItem = QTableWidgetItem("160")
        self.tableWidget.setItem(0, 2, newItem)

        newItem = QTableWidgetItem("李四")
        self.tableWidget.setItem(1, 0, newItem)

        newItem = QTableWidgetItem("女")
        self.tableWidget.setItem(1, 1, newItem)

        newItem = QTableWidgetItem("120")
        self.tableWidget.setItem(1, 2, newItem)

        # 允许右键产生菜单
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        # 将右键菜单绑定到槽函数generateMenu
        self.tableWidget.customContextMenuRequested.connect(self.generateMenu)

        layout = QHBoxLayout()

        layout.addWidget(self.tableWidget)

        self.setLayout(layout)

    def generateMenu(self, pos):
        # 计算有多少条数据，默认-1,
        row_num = -1
        for i in self.tableWidget.selectionModel().selection().indexes():
            row_num = i.row()

        # 表格中只有两条有效数据，所以只在前两行支持右键弹出菜单
        if row_num < 2:
            menu = QMenu()
            item1 = menu.addAction(u'选项一')
            item2 = menu.addAction(u'选项二')
            item3 = menu.addAction(u'选项三')
            action = menu.exec_(self.tableWidget.mapToGlobal(pos))
            # 显示选中行的数据文本
            if action == item1:
                print('你选了选项一，当前行文字内容是：', self.tableWidget.item(row_num, 0).text(),
                      self.tableWidget.item(row_num, 1).text(),
                      self.tableWidget.item(row_num, 2).text())
            if action == item2:
                print('你选了选项二，当前行文字内容是：', self.tableWidget.item(row_num, 0).text(),
                      self.tableWidget.item(row_num, 1).text(),
                      self.tableWidget.item(row_num, 2).text())
            if action == item3:
                print('你选了选项三，当前行文字内容是：', self.tableWidget.item(row_num, 0).text(),
                      self.tableWidget.item(row_num, 1).text(),
                      self.tableWidget.item(row_num, 2).text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Table()
    example.show()
    sys.exit(app.exec_())
