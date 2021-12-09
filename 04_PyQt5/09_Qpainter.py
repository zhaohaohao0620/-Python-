"""
    【简介】
    在窗体中绘画出文字的例子
"""

import math
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication, QWidget


class Drawing(QWidget):
    def __init__(self, parent=None):
        super(Drawing, self).__init__(parent)
        self.setWindowTitle("在窗体中绘画出文字例子")
        self.resize(300, 200)
        self.text = '欢迎学习 PyQt5'

    """ 绘制文字
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        # 自定义的绘画方法
        self.drawText(event, painter)
        painter.end()

    def drawText(self, event, qp):
        # 设置笔的颜色
        qp.setPen(QColor(168, 34, 3))
        # 设置字体
        qp.setFont(QFont('SimSun', 20))
        # 画出文本
        qp.drawText(event.rect(), Qt.AlignCenter, self.text)
    """

    # 绘制点
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        # 自定义画点方法
        self.drawPoints(qp)
        qp.end()

    def drawPoints(self, qp):
        qp.setPen(Qt.red)
        size = self.size()

        for i in range(1000):
            # [-100, 100]两个周期的正弦函数图像
            x = 100 * (-1 + 2.0 * i / 1000) + size.width() / 2.0
            y = -50 * math.sin((x - size.width() / 2.0) * math.pi / 50) + size.height() / 2.0
            qp.drawPoint(x, y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Drawing()
    demo.show()
    sys.exit(app.exec_())
