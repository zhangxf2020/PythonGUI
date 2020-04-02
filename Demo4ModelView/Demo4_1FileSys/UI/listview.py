from PyQt5.QtWidgets import QListView,QApplication,QWidget,QVBoxLayout,QFileSystemModel
from PyQt5.QtCore import QModelIndex,QDir

import sys


class myWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(1000,500,500,600)

        self.initUI()
        self.show()
    def initUI(self):
        layout = QVBoxLayout(self)
        mylistView = QListView(self)
        layout.addWidget(mylistView)
        model = QFileSystemModel(self)
        model.setRootPath(r'D:\工具')
        mylistView.setModel(model)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = myWidget()
    sys.exit(app.exec_())