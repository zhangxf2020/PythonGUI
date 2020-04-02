from PyQt5.QtWidgets import QApplication,QMainWindow,QFileSystemModel
from PyQt5.QtCore import QDir,QModelIndex

import sys
from ui_MainWindow import Ui_MainWindow

class QmyMainWindow(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__buildModelView()

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~自定义函数~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def __buildModelView(self):
        self.model = QFileSystemModel(self) #创建文件模型
        self.model.setRootPath(QDir.currentPath())#设置模型的根目录
        self.ui.treeView.setModel(self.model)#对treeview,listview,tableview设置模型
        self.ui.listView.setModel(self.model)
        self.ui.tableView.setModel(self.model)
        self.ui.treeView.clicked.connect(self.ui.listView.setRootIndex)#将点击返回的Qmodelindex作为顶层模型
        self.ui.treeView.clicked.connect(self.ui.tableView.setRootIndex)
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~自动创建的函数~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def on_treeView_clicked(self,index:QModelIndex):
        print(index.row())
        self.ui.checkBox.setChecked(self.model.isDir(index))
        self.ui.LabPath.setText(self.model.filePath(index))
        self.ui.LabFileName.setText(self.model.fileName(index))
        self.ui.label_3.setText(self.model.type(index))
        fileSize = self.model.size(index) / 1024
        if fileSize <1024:
            self.ui.LabFileSize.setText('{} KB'.format(fileSize))
        else:
            self.ui.LabFileSize.setText('{:.2f} MB'.format(fileSize / 1024))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyMainWindow()
    form.show()
    sys.exit(app.exec_())