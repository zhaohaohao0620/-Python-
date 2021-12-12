import sys

from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QCalendarWidget, QLabel, QApplication, QWidget


class CalendarExample(QWidget):
    def __init__(self):
        super(CalendarExample, self).__init__()
        self.initUI()

    def initUI(self):
        # 实例化日历控件
        self.cal = QCalendarWidget(self)
        # 设置日历的最小日期
        self.cal.setMinimumDate(QDate(1980, 1, 1))
        # 设置日历的最大日期
        self.cal.setMaximumDate(QDate(3000, 1, 1))
        # 设置日历的网格是否可见
        self.cal.setGridVisible(True)
        # 控件位置移动
        self.cal.move(20, 20)
        # 点击绑定自定义的槽函数
        self.cal.clicked[QtCore.QDate].connect(self.showDate)

        # 创建标签
        self.lb1 = QLabel(self)
        # 设置标签的文本为日历控件所选中的日期，并转为str数据显示
        date = self.cal.selectedDate()
        self.lb1.setText(date.toString('yyyy-MM-dd dddd'))

        # 标签移动位置
        self.lb1.move(20, 300)
        # 设置主窗口的位置及初始大小和标题
        self.setGeometry(200, 100, 400, 350)
        self.setWindowTitle('Calendar例子')

    def showDate(self, date):
        # 设置标签的文本值
        self.lb1.setText(date.toString('yyyy-MM-dd dddd'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = CalendarExample()
    demo.show()
    sys.exit(app.exec_())
