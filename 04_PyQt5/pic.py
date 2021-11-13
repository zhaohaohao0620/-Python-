from sys import argv, exit

from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg,
                                                NavigationToolbar2QT)
from matplotlib.pyplot import Figure, rcParams
from matplotlib.ticker import FuncFormatter
from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget

rcParams['xtick.direction'] = 'in'
rcParams['ytick.direction'] = 'in'
rcParams['font.sans-serif'] = 'SimHei'  ## 'Times New Roman'
rcParams['axes.unicode_minus'] = False

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.Common()
        self.ShowPic()
        self.DrawPicInCanvs()

    def Common(self):
        self.setGeometry(300, 50, 1000, 750)
        self.setWindowTitle('Demo')
        self.setFixedSize(self.width(), self.height())

    def ShowPic(self):
        self.fig = Figure()
        self.fig.clf()

        self.canvs = FigureCanvasQTAgg(self.fig)
        toolBar = NavigationToolbar2QT(self.canvs, self)

        grid = QGridLayout()
        grid.addWidget(self.canvs, 0, 0, 5, 1)
        grid.addWidget(toolBar, 5, 0)

        self.setLayout(grid)
    
    def DrawPicInCanvs(self):
        x = [10, 20, 30, 40, 50]
        y = [1000, 2000, 3000, 4000, 5000]

        self.fig.clf()

        ax = self.fig.add_subplot()
        ax.plot(x , y, linewidth = 0.5, color = '#0000ff')
        ax.grid(linestyle = '--')

        ax.xaxis.set_major_formatter(FuncFormatter(self.__PointToM))
        ax.yaxis.set_major_formatter(FuncFormatter(self.__GHzToMHz))

        self.canvs.draw()

    def __PointToM(self, tmp, poistion):
        return tmp*0.1
    
    def __GHzToMHz(self, tmp, poistion):
        return tmp/100

if __name__ == '__main__':
    app = QApplication(argv)
    demo = Demo()
    demo.show()
    exit(app.exec_())
