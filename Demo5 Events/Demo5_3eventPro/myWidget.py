# encoding= UTF-8
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox
import sys
from ui_Widget import Ui_Widget


class QmyWidget(QWidget):
    def __init__(self,parent = None):
        super(QmyWidget, self).__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

    def event(self, event:QEvent) -> bool:
        eventType = event.type()
        print('event.type() = {}'.format(eventType)) #监视所有事件的id
        if event.type() == QEvent.Paint : #如果event类型是绘制操作,则屏蔽重载的绘制函数
            return True #返回True退出事件处理
        elif event.type() ==QEvent.KeyRelease and event.key() == Qt.Key_Tab:#如果
            rect = self.ui.btnMove.geometry()
            self.ui.btnMove.setGeometry(rect.x()+100,rect.y(),rect.width(),rect.height())

        return super().event(event)

    def paintEvent(self, a0:QPaintEvent) -> None:#绘制窗口背景图片
        painter = QPainter(self)
        pic = QPixmap(r'Resource/images/sea1.jpg')
        painter.drawPixmap(0,0,self.width(),self.height(),pic)
        super().paintEvent(a0)
    def resizeEvent(self, a0:QResizeEvent) -> None:#尺寸大小改变时触发
        W = self.width()
        H = self.height()
        Wbtn = self.ui.btnTest.width()
        Hbtn = self.ui.btnTest.height()

        self.ui.btnTest.setGeometry(int((W - Wbtn)/2),int((H-Hbtn)/2),Wbtn,Hbtn)
        super().resizeEvent(a0)
    def closeEvent(self, a0:QCloseEvent) -> None: #关闭窗口时触发
        dlgTitle = 'Question消息框'
        strInfo = 'CloseEvent事件触发,确定要退出吗?'
        result = QMessageBox.question(self,dlgTitle,strInfo,QMessageBox.Yes |QMessageBox.No,QMessageBox.NoButton)
        if result ==QMessageBox.Yes:
            a0.accept()#同意,消息现在处理,不往上分发
        else:
            a0.ignore()#否定,消息往上分发
    def mousePressEvent(self, a0:QMouseEvent) -> None:#鼠标点击触发
        print(a0.windowPos())
        print(a0.localPos())
        print(a0.globalPos())#返回全局坐标
        if a0.button() == Qt.LeftButton:
            self.ui.LabelMove.setText('(x, y) → ({}, {})'.format(a0.x(),a0.y()))
            self.ui.LabelMove.setGeometry(a0.x(),a0.y(),self.ui.LabelMove.width(),self.ui.LabelMove.height())
        super().mousePressEvent(a0)
    def keyPressEvent(self, event:QKeyEvent) -> None:#按键按下触发
        rect = self.ui.btnMove.geometry()
        print(rect.x())
        if event.key() in set([Qt.Key_A,Qt.Key_Left]):
            self.ui.btnMove.setGeometry(rect.x() -20,rect.top(),rect.width(),rect.height())
        elif event.key() in set([Qt.Key_Right,Qt.Key_D]):
            self.ui.btnMove.setGeometry(rect.x()+20,rect.top(),rect.width(),rect.height())
        elif event.key() in set([Qt.Key_Up, Qt.Key_W]):
            self.ui.btnMove.setGeometry(rect.x(), rect.y()-20, rect.width(), rect.height())
        elif event.key() in set([Qt.Key_Down, Qt.Key_S]):
            self.ui.btnMove.setGeometry(rect.x(), rect.y()+20, rect.width(), rect.height())
    def hideEvent(self, event:QHideEvent) -> None: #窗口最小化触发
        print('hideEvent 事件触发')

    def showEvent(self, event:QShowEvent) -> None:#窗体显示时触发
        print('showEvent 事件触发')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())
