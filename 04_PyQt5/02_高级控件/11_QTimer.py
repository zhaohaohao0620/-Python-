import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QListWidget, QGridLayout, QLabel
from PyQt5.QtCore import QTimer, QDateTime, Qt


class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        # 设置标题
        self.setWindowTitle('QTimer demo')

        # 实例化一些控件
        self.listFile = QListWidget()
        self.lable = QLabel('显示当前时间')
        self.startBtn = QPushButton('开始')
        self.endBtn = QPushButton('结束')

        # 栅格布局
        layout = QGridLayout()

        # 初始化一个定时器
        self.timer = QTimer()
        # 定时器结束，触发showTime方法
        self.timer.timeout.connect(self.show_time)

        # 添加控件到栅格指定位置
        layout.addWidget(self.lable, 0, 0, 1, 2)
        layout.addWidget(self.startBtn, 1, 0)
        layout.addWidget(self.endBtn, 1, 1)

        # 开始结束按钮点击触发相应的槽函数
        self.startBtn.clicked.connect(self.start_timer)
        self.endBtn.clicked.connect(self.end_timer)

        # 设置布局方式
        self.setLayout(layout)

    def show_time(self):
        # 获取系统当前时间
        time = QDateTime.currentDateTime()
        # 设置系统时间的显示格式
        timeDisplay = time.toString('yyyy-MM-dd hh:mm:ss dddd')
        # 在标签上显示时间
        self.lable.setText(timeDisplay)

    def start_timer(self):
        # 设置时间间隔并启动定时器
        self.timer.start(1000)
        # 设置开始按钮不可点击，结束按钮可点击
        self.startBtn.setEnabled(False)
        self.endBtn.setEnabled(True)

    def end_timer(self):
        # 停止定时器
        self.timer.stop()
        # 结束按钮不可点击，开始按钮可以点击
        self.startBtn.setEnabled(True)
        self.endBtn.setEnabled(False)


if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # form = WinForm()
    # form.show()
    # sys.exit(app.exec_())

    app = QApplication(sys.argv)
    # 设置标签以及文本内容
    label = QLabel('<font color=red size=128><b>Hello PyQt,窗口会在10秒后消失！</b></font>')
    # 设置无边框窗口
    label.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)

    label.show()

    # 设置10秒后自动退出
    QTimer.singleShot(10000, app.quit)

    sys.exit(app.exec_())
