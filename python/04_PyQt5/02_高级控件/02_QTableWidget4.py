import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QHBoxLayout, QTableWidget, QAbstractItemView, QTableWidgetItem, QApplication, QWidget


class Table(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置标题与初始大小
        self.setWindowTitle("QTableWidget 例子")
        self.resize(1000, 900)
        # 设置布局，初始表格5*3
        conLayout = QHBoxLayout()
        table = QTableWidget(5, 3)

        # 设置表格水平头标签
        table.setHorizontalHeaderLabels(['图片1', '图片2', '图片3'])
        # 设置不可编辑模式
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 设置图片的大小
        table.setIconSize(QSize(300, 200))

        # 设置所有行列宽高数值与图片大小相同
        for i in range(3):  # 让列宽和图片相同
            table.setColumnWidth(i, 300)
        for i in range(5):  # 让行高和图片相同
            table.setRowHeight(i, 200)

        for k in range(15):
            i = k / 3
            j = k % 3

            # 实例化表格窗口条目
            item = QTableWidgetItem()
            # 用户点击表格时，图片被选中
            item.setFlags(Qt.ItemIsEnabled)
            # 图片路径设置与图片加载
            icon = QIcon(r'./../../images/bao%d.png' % k)
            item.setIcon(QIcon(icon))
            # 输出当前进行的条目序号
            print('e/icons/%d.png i=%d  j=%d' % (k, i, j))
            # 将条目加载到相应行列中
            table.setItem(i, j, item)

        conLayout.addWidget(table)
        self.setLayout(conLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Table()
    example.show()
    sys.exit(app.exec_())
