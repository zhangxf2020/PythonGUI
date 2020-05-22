import sys,random
from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QDialog
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtCore import QItemSelectionModel,pyqtSignal,QModelIndex,pyqtSlot,Qt

from ui_MainWindow import Ui_MainWindow
from myDialogLocate import QmyDialogLocate
from myDialogSize import QmyDialogSize
from myDialogHeaders import QmyDialogHeaders


class QmyMainWindow(QMainWindow):
    cellIndexChanged = pyqtSignal(int,int)
    def __init__(self,parent = None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #创建状态栏
        self.LabCellPos = QLabel('当前单元格',self)
        self.LabCellPos.setMinimumWidth(180)
        self.ui.statusBar.addWidget(self.LabCellPos)

        self.LabCellText = QLabel('当前单元格内容',self)
        self.LabCellText.setMinimumWidth(180)
        self.ui.statusBar.addWidget(self.LabCellText)
        #构建数据模型
        self.dataModel = QStandardItemModel(6,5,self)
        self.chooseModel = QItemSelectionModel(self.dataModel)
        self.ui.tableView.setModel(self.dataModel)
        self.ui.tableView.setSelectionModel(self.chooseModel)

        self.chooseModel.currentChanged.connect(self.do_indexchanged)
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~自动生成的函数~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #定位单元格
    @pyqtSlot()
    def on_actTab_Locate_triggered(self):
        dwSelectIndex = QmyDialogLocate(self)
        dwSelectIndex.setRanges(self.dataModel.rowCount(),self.dataModel.columnCount())
        dwSelectIndex.changeCellText.connect(self.do_setACellText)
        self.cellIndexChanged.connect(dwSelectIndex.do_setSpinValue)
        dwSelectIndex.setAttribute(Qt.WA_DeleteOnClose)
        dwSelectIndex.show()

    @pyqtSlot()
    def on_actTab_SetSize_triggered(self):
        setranks = QmyDialogSize()
        setranks.do_setRanks(self.dataModel.rowCount(),self.dataModel.columnCount())
        ret = setranks.exec()
        if ret ==QDialog.Accepted:
            rows,cols = setranks.getRanks()
            self.dataModel.setRowCount(rows)
            rowstrlist = ['河南','河北','山东','山西','广东','广西']
            for i in range(rows):
                strtext = random.choice(rowstrlist)
                rowstrlist.append(strtext)
            self.dataModel.setHorizontalHeaderLabels(rowstrlist)
            self.dataModel.setColumnCount(cols)
    @pyqtSlot()
    def on_actTab_SetHeader_triggered(self):
        headers = QmyDialogHeaders()
        strlist =[]
        for i in range(self.dataModel.columnCount()):
            text = str(self.dataModel.headerData(i,Qt.Horizontal,Qt.DisplayRole))
            strlist.append(text)
        headers.setHeaderList(strlist)
        res = headers.exec()
        if res == QDialog.Accepted:
            strlist = headers.headerList()
            self.dataModel.setHorizontalHeaderLabels(strlist)


    def do_indexchanged(self,current:QModelIndex,previous:QModelIndex):
        self.cellIndexChanged.emit(current.row(),current.column())
        item = self.dataModel.itemFromIndex(current)
        if not current ==None:
            self.LabCellPos.setText('{}  {}'.format(current.row(),current.column()))
            self.LabCellText.setText(item.text())


    def do_setACellText(self,row,column,text):
        index = self.dataModel.index(row,column)
        self.chooseModel.clearSelection()
        self.chooseModel.setCurrentIndex(index,QItemSelectionModel.Select)
        self.dataModel.setData(index,text,Qt.DisplayRole)

    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~自定义功能函数~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mymainwindow = QmyMainWindow()
    mymainwindow.show()
    sys.exit(app.exec_())