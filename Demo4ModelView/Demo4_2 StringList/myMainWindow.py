from PyQt5.QtWidgets import QMainWindow,QApplication,QAbstractItemView
from PyQt5.QtCore import QStringListModel,pyqtSlot,Qt

import sys
from ui_MainWindow import Ui_MainWindow

class QmyMainWindow(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__provinces =['北京','上海','天津','河北','山东','四川','重庆','广东','河南']
        self.model = QStringListModel(self.__provinces)
        self.ui.listView.setModel(self.model)
        self.ui.listView.setEditTriggers(QAbstractItemView.SelectedClicked | QAbstractItemView.DoubleClicked ) #设置什么时候可以编辑列表,这里是选择单击或是直接双击
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~自动生成的函数~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #还原数据
    @pyqtSlot()
    def on_btn_ResList_clicked(self):
        self.model.setStringList(self.__provinces)
    #添加数据
    @pyqtSlot()
    def on_btn_AddIns_clicked(self):
        lastRow = self.model.rowCount()#计算模型数据的总行数
        self.model.insertRow(lastRow)#在模型最后一行中插入空白list
        index = self.model.index(lastRow,0)#拿到最后一行的索引
        self.model.setData(index,'new item',Qt.DisplayRole)#往索引中添加数据
        self.ui.listView.setCurrentIndex(index)#设置当前选中行
    #插入项
    @pyqtSlot()
    def on_btn_insertItem_clicked(self):
        index = self.ui.listView.currentIndex()#返回所选择项的 模型索引
        if index.row()<0:
            index = self.model.index(0)
        self.model.insertRow(index.row())
        self.model.setData(index,'inster item',Qt.DisplayRole)
        self.ui.listView.setCurrentIndex(index)
    #删除项
    @pyqtSlot()
    def on_btn_DelCurrentItem_clicked(self):
        index = self.ui.listView.currentIndex()
        self.model.removeRow(index.row())

    # 清空项
    @pyqtSlot()
    def on_btn_EmptyList_clicked(self):
        rowCount = self.model.rowCount()
        self.model.removeRows(0,rowCount)#从第几项开始到第几项(不包含最终)
    #清空文本
    @pyqtSlot()
    def on_btn_ClearText_clicked(self):
        self.ui.textEdit.clear()

    #以文本显示数据模型内容
    @pyqtSlot()
    def on_btn_TextDisplay_clicked(self):
        self.ui.textEdit.clear()
        strList = self.model.stringList()
        for strLine in strList:
            self.ui.textEdit.appendPlainText(strLine)
    #添加状态信息
    def on_listView_clicked(self,index):
        self.ui.LabInfo.setText('当前项: row = {},  column = {}'.format(index.row(),index.column()))





if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyMainWindow()
    form.show()
    sys.exit(app.exec_())




