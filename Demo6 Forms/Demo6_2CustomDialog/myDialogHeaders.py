import sys
from ui_QWDialogHeaders import Ui_QWDialogHeaders
from PyQt5.QtWidgets import QDialog,QApplication,QAbstractItemView
from PyQt5.QtCore import QStringListModel,Qt
# from PyQt5.QtGui import

class QmyDialogHeaders(QDialog):
    def __init__(self,parent =None):
        super().__init__(parent)
        self.ui = Ui_QWDialogHeaders()
        self.ui.setupUi(self)

        self.__model = QStringListModel()
        self.ui.listView.setModel(self.__model)

        self.ui.listView.setAlternatingRowColors(True)#开启交替颜色背景
        self.ui.listView.setDragDropMode(QAbstractItemView.InternalMove)#控制视图拖放事件的处理方式(不是拷贝)
        self.ui.listView.setDefaultDropAction(Qt.MoveAction)#视图放下事件的处理方式(从拖动点移动到鼠标释放处)
    def setHeaderList(self,headerStrList):
        self.__model.setStringList(headerStrList)#设置模型数据
    def headerList(self):
        return self.__model.stringList()#返回模型数据

    def __del__(self):
        print("QmyDialogHeaders 对象被删除了")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyDialogHeaders()
    form.show()
    sys.exit(app.exec_())