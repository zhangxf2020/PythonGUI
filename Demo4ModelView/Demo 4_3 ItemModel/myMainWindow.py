from PyQt5.QtWidgets import QApplication,QMainWindow,QAbstractItemView,QFileDialog,QLabel
from PyQt5.QtCore import Qt,pyqtSlot,QItemSelectionModel,QDir,QModelIndex
from PyQt5.QtGui import QStandardItemModel,QStandardItem
import sys,os
from ui_MainWindow import Ui_MainWindow

class QmyMainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(QmyMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__ColCount = 6
        self.itemModel = QStandardItemModel(5,self.__ColCount)
        self.selectionModel = QItemSelectionModel(self.itemModel)
        self.selectionModel.currentChanged.connect(self.do_curChanged)


        self.ui.tableView.setModel(self.itemModel)
        self.ui.tableView.setSelectionModel(self.selectionModel)
        self.ui.tableView.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.__buildStatusBar()

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~自定义功能函数~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __buildStatusBar(self):
        self.LabCellPos = QLabel('当前单元格',self)
        self.LabCellPos.setMinimumWidth(180)
        self.ui.statusbar.addWidget(self.LabCellPos)

        self.LabCellText = QLabel('单元格内容',self)
        self.LabCellText.setMinimumWidth(150)
        self.ui.statusbar.addWidget(self.LabCellText)

        self.LabCurFile = QLabel('当前文件',self)
        self.ui.statusbar.addPermanentWidget(self.LabCurFile)

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~自定义槽函数~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def do_curChanged(self,current:QModelIndex,previous:QModelIndex):
        if current !=None:
            text = '当前单元格: {} 行, {} 列'.format(current.row(),current.column())
            self.LabCellPos.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyMainWindow()
    form.show()
    sys.exit(app.exec_())
        