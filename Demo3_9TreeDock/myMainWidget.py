from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QDockWidget,QMenu,QTreeWidgetItem,QFileDialog
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import pyqtSlot,Qt,QDir,QFileInfo
from enum import Enum
import sys
from ui_MainWidget import Ui_MainWindow

class TreeItemType(Enum):
    itTopItem = 1001
    itGroupItem = 1002
    itImageItem = 1003

class TreeColNum(Enum):
    colItem = 0
    colItemType = 1

class QmyMainWidget(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.scrollArea)

        self.ui.dockWidget.setFeatures(QDockWidget.AllDockWidgetFeatures)#设置停靠窗口上的小按钮显示(关闭/折叠等)
        self.ui.dockWidget.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)#设置停靠窗口的停靠位置,这里是左右

        #自动滚动区域控件Qscrollarea,其中包含一个Qwidget控件
        self.ui.scrollArea.setWidgetResizable(True)#设置自动滚动区控件的尺寸为自适应
        self.ui.scrollArea.setAlignment(Qt.AlignCenter)#设置自动滚动区域对其方式,居中
        self.ui.LabPicture.setAlignment(Qt.AlignCenter)#设置图片标签控件对其方式,居中

        self.itemFlags = Qt.ItemIsSelectable | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled | Qt.ItemIsAutoTristate
        self.__initTree()

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~优雅的分割线~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #初始化目录树
    def __initTree(self):
        self.ui.treeFiles.clear()
        icon = QIcon(r':icons/icons/15.ico')

        item = QTreeWidgetItem(TreeItemType.itTopItem.value)
        item.setIcon(TreeColNum.colItem.value,icon)
        item.setText(TreeColNum.colItem.value,'图片文件')
        item.setFlags(self.itemFlags)
        item.setCheckState(TreeColNum.colItem.value,Qt.Checked)
        item.setData(TreeColNum.colItem.value,Qt.UserRole,'')
        self.ui.treeFiles.addTopLevelItem(item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyMainWidget()
    form.show()
    sys.exit(app.exec_())