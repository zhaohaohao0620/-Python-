from PyQt5.QtCore import QObject,pyqtSignal


class SignalClass(QObject):
    #声明无参数的信号
    signal1=pyqtSignal()
    #声明带一个int类型参数的信号
    signal2=pyqtSignal(int)

    def __init__(self,parent=None):
        super(SignalClass, self).__init__(parent)
        #将signal1信号连接到两个槽函数
        self.signal1.connect(self.sig1Call)
        self.signal1.connect(self.sig2Call)

        #将signal2信号连接到信号1
        self.signal2.connect(self.signal1)

        #发射信号
        self.signal1.emit()
        self.signal2.emit(1)

        #断开信号与槽函数的关系
        self.signal1.disconnect(self.sig1Call)
        self.signal1.disconnect(self.sig2Call)
        self.signal2.disconnect(self.signal1)

        #绑定信号与槽函数
        self.signal1.connect(self.sig1Call)
        self.signal2.connect(self.sig1Call)

        #信号发射
        self.signal1.emit()
        self.signal2.emit(1)
    #输出信号1发射
    def sig1Call( self ):
        print('signal-1 emit')
    #输出信号2发射
    def sig2Call( self ):


        print('signal-2 emit')
if __name__ == '__main__':
    signal=SignalClass()