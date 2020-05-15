from PyQt5.QtGui import QDragEnterEvent, QDropEvent,QPixmap
from PyQt5.QtWidgets import QApplication,QWidget

import sys,os
from ui_Widget import Ui_Widget

class QmyWidget(QWidget):
    def __init__(self,parent = None):
        super(QmyWidget, self).__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.setAcceptDrops(True)
        self.ui.plainTextEdit.setAcceptDrops(False)#不允许放置
        self.ui.LabPic.setAcceptDrops(False)
        self.ui.LabPic.setScaledContents(True) #图片适应标签大小
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~事件处理函数~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def dragEnterEvent(self, event:QDragEnterEvent) -> None:
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.appendPlainText('dragEnterEvent事件 mimeData() ->formats()')
        for strLine in event.mimeData().formats():#格式数据
            print(strLine)
            self.ui.plainTextEdit.appendPlainText(strLine)

        self.ui.plainTextEdit.appendPlainText('\ndragEnterEvent事件 mimeData() ->urls()')
        for url in event.mimeData().urls(): #地址数据
            self.ui.plainTextEdit.appendPlainText(url.path())

        if event.mimeData().hasUrls():#如果含有urls
            filename = event.mimeData().urls()[0].fileName()#得到第一个地址的文件名称
            basename,ext = os.path.splitext(filename)#返回名称和后缀
            ext = ext.upper()#转换为大写
            if ext =='.JPG':
                event.acceptProposedAction() #接受放置操作
            else:
                event.ignore()
        else:
            event.ignore()
    def dropEvent(self, event:QDropEvent) -> None:#放置事件
        filename = event.mimeData().urls()[0].path()
        cnt = len(filename)
        realname = filename[1:cnt]
        pixmap = QPixmap(realname)
        self.ui.LabPic.setPixmap(pixmap)
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())