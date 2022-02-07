import sys

from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtWidgets import QWidget, QLabel, QScrollBar, QApplication, QHBoxLayout


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        # 水平布局
        HBox = QHBoxLayout()

        # 创建标签以及显示文本，设置字体类型和字号大小
        self.l1 = QLabel('拖动滑块改变颜色')
        self.l1.setFont(QFont('Arial', 16))

        # 添加到布局中
        HBox.addWidget(self.l1)

        # 创建滑块，设置最大值，滑动信号关联到槽函数
        # 水平滚动 QScrollBar(Qt.Horizontal,self)
        self.s1 = QScrollBar()
        self.s1.setMaximum(255)
        self.s1.sliderMoved.connect(self.slider_val)

        self.s2 = QScrollBar()
        self.s2.setMaximum(255)
        self.s2.sliderMoved.connect(self.slider_val)

        self.s3 = QScrollBar()
        self.s3.setMaximum(255)
        self.s3.sliderMoved.connect(self.slider_val)

        # 添加部件到布局中
        HBox.addWidget(self.s1)
        HBox.addWidget(self.s2)
        HBox.addWidget(self.s3)

        # 初始化位置以及初始窗口大小，设置整体布局方式和标题
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QScrollBar例子')
        self.setLayout(HBox)

    def slider_val(self):
        # 输出当前三个滑块位置所代表的值
        print(self.s1.value(), self.s2.value(), self.s3.value())

        # 实例化调色板对象，设置颜色为三个滑块的值
        palette = QPalette()
        c = QColor(self.s1.value(), self.s2.value(), self.s3.value())
        palette.setColor(QPalette.Foreground, c)

        # 设置标签的调色板，加载属性
        self.l1.setPalette(palette)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Example()
    demo.show()
    sys.exit(app.exec_())
