import sys

from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('加载本地网页的例子')
        self.setGeometry(5, 30, 1355, 730)
        self.browser = QWebEngineView()
        # #加载外部的web界面
        # url=r'index.html'
        # self.browser.load(QUrl(url))

        self.browser.setHtml('''<!DOCTYPE html>
                                <html lang="en">
                                <head>
                                    <meta charset="UTF-8">
                                    <title>Title</title>
                                </head>
                                <body>
                                <h1>Hello PyQt5</h1>
                                <h1>Hello PyQt5</h1>
                                <h1>Hello PyQt5</h1>
                                <h1>Hello PyQt5</h1>
                                <h1>Hello PyQt5</h1>

                                </body>
                                </html>''')
        self.setCentralWidget(self.browser)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exit(app.exec_())
