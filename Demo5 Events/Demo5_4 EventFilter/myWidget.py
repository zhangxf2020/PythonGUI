from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import QEvent
import sys
from ui_myWidget import Ui_Widget

class QmyWidget(QWidget):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.label.installEventFilter(self)
        self.ui.label_2.installEventFilter(self) #安装事件过滤器,不安装的话,窗口实例中只对已安装的过滤器的控件进行监测
        
    def eventFilter(self, a0: 'QObject', a1: 'QEvent') -> bool:
        if a0 == self.ui.label:
            if a1.type() == QEvent.Enter:#光标进入
                self.ui.label.setStyleSheet('background-color: rgb(170,255,255)')
                self.ui.label.setText('鼠标进入了标签')
            elif a1.type() == QEvent.Leave:#光标移出
                self.ui.label.setStyleSheet('')
                self.ui.label.setText('鼠标移出了标签')
            elif a1.type() ==QEvent.MouseButtonPress:
                self.ui.label.setText('鼠标按下了')
            elif a1.type() == QEvent.MouseButtonRelease:
                self.ui.label.setText('鼠标松开了')
        elif a0 == self.ui.label_2:
            if a1.type() ==QEvent.Enter:
                self.ui.label_2.setStyleSheet('background-color: rgb(85,255,127)')
                self.ui.label_2.setText('鼠标进入了标签')
            elif a1.type() == QEvent.Leave:
                self.ui.label_2.setStyleSheet('')
                self.ui.label_2.setText('鼠标离开了标签')
            elif a1.type() == QEvent.MouseButtonDblClick:#鼠标双击
                self.ui.label_2.setText('鼠标双击了标签')
        return super(QmyWidget, self).eventFilter(a0,a1)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())

        