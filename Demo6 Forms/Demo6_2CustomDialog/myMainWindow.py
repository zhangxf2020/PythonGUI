import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QDialog
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtCore import QItemSelectionModel,pyqtSignal,QModelIndex,pyqtSlot,Qt

from ui_MainWindow import Ui_MainWindow
from myDialogSize import QmyDialogSize
from myDialogHeaders import  QmyDialogHeaders
from myDialogLocate import QmyDialogLocate

class QmyMainWindow(QMainWindow):
    cellIndexChanged = pyqtSignal(int,int)
    def __init__(self,parent = None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__dlgSetHeaders = None
        self.setCentralWidget(self.ui.tableView)

        #创建状态栏
        self.LabCellPos = QLabel('当前单元格',self)
        self.LabCellPos.setMinimumWidth(180)
        self.ui.statusBar.addWidget(self.LabCellPos)

        self.LabCellText = QLabel('当前单元格内容',self)
        self.LabCellText.setMinimumWidth(180)
        self.ui.statusBar.addWidget(self.LabCellText)
        #构建数据模型
        self.itemModel = QStandardItemModel(10,5,self)#数据模型,10行5列
        self.selectionModel = QItemSelectionModel(self.itemModel)#item选择模型
        self.selectionModel.currentChanged.connect(self.do_currentChanged)

        #为view设置模型
        self.ui.tableView.setModel(self.itemModel)#设置数据模型
        self.ui.tableView.setSelectionModel(self.selectionModel)#设置选择模型\
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~自动生成的函数~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #设置行/列数对话框
    @pyqtSlot()
    def on_actTab_SetSize_triggered(self):
        dlgTableSize = QmyDialogSize()
        dlgTableSize.setIniSize(self.itemModel.rowCount(),self.itemModel.columnCount())
        ret = dlgTableSize.exec()#模态方式运行对话框(此代码返回用户的响应结果,如果选择确定,返回QDialog.Accepted
        #如果选择取消,则返回QDialog.Rejected)
        if ret == QDialog.Accepted:#代表用户选择了确定
            rows,cols = dlgTableSize.getTableSize()#获得模型的行数和列数
            self.itemModel.setRowCount(rows)
            self.itemModel.setColumnCount(cols)
    #设置表头标题
    @pyqtSlot()
    def on_actTab_SetHeader_triggered(self):
        if self.__dlgSetHeaders==None:#检查是否存在对话窗对象
            self.__dlgSetHeaders = QmyDialogHeaders()#如果没有则新创建一个对象
        count = len(self.__dlgSetHeaders.headerList())#得到对象view模型的字符串模型列表数量
        if count !=self.itemModel.columnCount():#如果列表数量与当前模型列数不一致
            strList =[]
            for i in range(self.itemModel.columnCount()):
                text = str(self.itemModel.headerData(i,Qt.Horizontal,Qt.DisplayRole))#获得模型中的item数据(,增长方向,返回模式(字符串/图标等))
                strList.append(text)
            self.__dlgSetHeaders.setHeaderList(strList)
        ret = self.__dlgSetHeaders.exec()
        if ret == QDialog.Accepted:
            strList2 = self.__dlgSetHeaders.headerList()
            self.itemModel.setHorizontalHeaderLabels(strList2)
    #定位单元格
    @pyqtSlot()
    def on_actTab_Locate_triggered(self):
        dlgLocate = QmyDialogLocate(self)
        dlgLocate.setSpinRange(self.itemModel.rowCount(),self.itemModel.columnCount())
        dlgLocate.changeActionEnable.connect(self.do_setActLocateEnable)
        dlgLocate.changeCellText.connect(self.do_setACellText)
        self.cellIndexChanged.connect(dlgLocate.do_setSpinValue)
        dlgLocate.setAttribute(Qt.WA_DeleteOnClose)
        dlgLocate.show()



    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~自定义功能函数~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def do_currentChanged(self,current:QModelIndex,previous:QModelIndex):
        if current !=None: #如果当前选择模型索引存在
            self.LabCellPos.setText('当前单元格: {}行, {}列'.format(current.row(),current.column()))#显示索引的行和列
            item = self.itemModel.itemFromIndex(current)#从索引获得单元格对象
            self.LabCellText.setText('单元格内容:'+item.text())#显示单元格内容
            self.cellIndexChanged.emit(current.row(),current.column())#同时发射自定义信号,传出单元格对象索引位置
    def do_setActLocateEnable(self,enable):
        self.ui.actTab_Locate.setEnabled(enable)
    def do_setACellText(self,row,column,text):
        index = self.itemModel.index(row,column)
        # self.selectionModel.clearSelection()
        # self.selectionModel.setCurrentIndex(index,QItemSelectionModel.Select)
        self.itemModel.setData(index,text,Qt.DisplayRole)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mymainwindow = QmyMainWindow()
    mymainwindow.show()
    sys.exit(app.exec_())