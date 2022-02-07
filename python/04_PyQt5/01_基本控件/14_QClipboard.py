import sys

from PyQt5.QtCore import QMimeData
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QPushButton, QLabel, QGridLayout, QApplication


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        # 创建复制粘贴按钮，并添加快捷键
        textCopyButton = QPushButton("&Copy Text")
        textPasteButton = QPushButton("Paste &Text")
        htmlCopyButton = QPushButton("C&opy HTML")
        htmlPasteButton = QPushButton("Paste &HTML")
        imageCopyButton = QPushButton("Co&py Image")
        imagePasteButton = QPushButton("Paste &Image")

        # 创建文本标签和图像标签，显示文本和图像
        self.textLabel = QLabel("Original text")
        self.imageLabel = QLabel()
        self.imageLabel.setPixmap(QPixmap("./../../images/python.png"))

        # 设置栅格布局，并添加部件到相应的位置
        layout = QGridLayout()
        layout.addWidget(textCopyButton, 0, 0)
        layout.addWidget(imageCopyButton, 0, 1)
        layout.addWidget(htmlCopyButton, 0, 2)
        layout.addWidget(textPasteButton, 1, 0)
        layout.addWidget(imagePasteButton, 1, 1)
        layout.addWidget(htmlPasteButton, 1, 2)
        layout.addWidget(self.textLabel, 2, 0, 1, 2)
        layout.addWidget(self.imageLabel, 2, 2)

        # 设置主窗口的布局，自定义槽函数，设置标题
        self.setLayout(layout)
        textCopyButton.clicked.connect(self.copyText)
        textPasteButton.clicked.connect(self.pasteText)
        htmlCopyButton.clicked.connect(self.copyHtml)
        htmlPasteButton.clicked.connect(self.pasteHtml)
        imageCopyButton.clicked.connect(self.copyImage)
        imagePasteButton.clicked.connect(self.pasteImage)
        self.setWindowTitle("Clipboard 例子")

    def copyText(self):
        # 实例化剪切板，设置剪切板的文本
        clipboard = QApplication.clipboard()
        clipboard.setText("I've been clipped!")

    def pasteText(self):
        # 实例化剪切板，标签设置为剪切板的文本并显示
        clipboard = QApplication.clipboard()
        self.textLabel.setText(clipboard.text())

    def copyImage(self):
        # 实例化剪切板，设置剪切板加载的图想路径
        clipboard = QApplication.clipboard()
        clipboard.setPixmap(QPixmap("./../../images/python.png"))

    def pasteImage(self):
        # 实例化剪切板，z设置图像标签的图片加载，从剪切板获取路径
        clipboard = QApplication.clipboard()
        self.imageLabel.setPixmap(clipboard.pixmap())

    def copyHtml(self):
        # 实例化MimeData数据类型，设置类型Html的文本
        mimeData = QMimeData()
        mimeData.setHtml("<b>Bold and <font color=red>Red</font></b>")
        # 实例化剪切板，设置MimeData的初值文本
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mimeData)

    def pasteHtml(self):
        # 实例化剪切板，，获取MimeData的数据，并设置为标签的文本值
        clipboard = QApplication.clipboard()
        mimeData = clipboard.mimeData()
        if mimeData.hasHtml():
            self.textLabel.setText(mimeData.html())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())
