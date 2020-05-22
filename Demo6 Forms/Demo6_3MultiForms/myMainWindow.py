import sys
from PyQt5.QtWidgets import QMainWindow,QWidget,QApplication,QTableWidget
from PyQt5.QtCore import Qt,pyqtSlot
from PyQt5.QtGui import QPixmap,QPainter
from ui_MainWindow import Ui_MainWindow
from myQWFormDoc import QmyQWFormDoc
class QmyMainWindow(QMainWindow):
    def __init__(self,parent = None):
        super(QmyMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tabWidget.setTabsClosable(True)#TAB有关闭按钮
        self.ui.tabWidget.setDocumentMode(True)#标签显示模式,设置此属性后，不会呈现选项卡小部件框架。此模式对于显示文档类型页面很有用，该页面涵盖了大多数选项卡小部件区域。
        self.setWindowState(Qt.WindowMaximized)#窗口最大化显示
        self.setAutoFillBackground(True)#自动绘制背景
        self.setCentralWidget(self.ui.tabWidget)
        self.ui.tabWidget.clear()
        self.ui.tabWidget.setHidden(True)
        self.__pic = QPixmap('sea1.jpg')
    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        painter.drawPixmap(0,self.ui.toolBar.height(),self.width(),self.height()-self.ui.toolBar.height()-self.ui.statusbar.height(),self.__pic)
        super().paintEvent(event)
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~自动连接的函数~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    @pyqtSlot()
    def on_embedded_Widget_triggered(self):
        formDoc = QmyQWFormDoc(self)
        formDoc.setAttribute(Qt.WA_DeleteOnClose)
        title = 'Doc {}'.format(self.ui.tabWidget.count())
        curIndex = self.ui.tabWidget.addTab(formDoc,title)
        self.ui.tabWidget.setCurrentIndex(curIndex)
        self.ui.tabWidget.setHidden(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyMainWindow()
    form.show()
    sys.exit(app.exec_())
