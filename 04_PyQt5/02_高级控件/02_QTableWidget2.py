import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QTableWidget, QHBoxLayout, QApplication, QWidget, QTableWidgetItem, QHeaderView


class Table(QWidget):
    def __init__(self):
        super(Table, self).__init__()
        self.initUI()

    def initUI(self):
        # 设置标题与初始大小
        self.setWindowTitle('QTableWidget例子')
        self.resize(600, 800)

        # 实例化表格视图（30*4）
        table_widget = QTableWidget(30, 4)
        table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for i in range(30):
            for j in range(4):
                itemContent = '(%d,%d)' % (i, j)
                # 为每个表格内添加数据
                table_widget.setItem(i, j, QTableWidgetItem(itemContent))

        layout = QHBoxLayout()

        layout.addWidget(table_widget)

        self.setLayout(layout)

        # 遍历表格查找对应项
        text = '(10,1)'
        items = table_widget.findItems(text, Qt.MatchExactly)
        item = items[0]
        # 选中单元格
        item.setSelected(True)
        # 设置单元格的背脊颜色为红
        item.setForeground(QBrush(QColor(255, 0, 0)))

        row = item.row()
        # 通过鼠标滚轮定位，快速定位到第十一行
        table_widget.verticalScrollBar().setSliderPosition(row)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    table = Table()
    table.show()
    sys.exit(app.exec_())
