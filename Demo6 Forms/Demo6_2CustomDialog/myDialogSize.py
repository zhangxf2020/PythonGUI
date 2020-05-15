from ui_QWDialogSize import Ui_QWDialogSize
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5.QtCore import Qt
import sys

class QmyDialogSize(QDialog):
    def __init__(self,rowCount = 3,colCount = 5,parent= None):
        super().__init__(parent)
        self.ui = Ui_QWDialogSize()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)#固定窗口大小
        self.setIniSize(rowCount,colCount)#设置两个步长调节器初始值
    def setIniSize(self,rowCount,colCount):
        self.ui.spin_RwoCount.setValue(rowCount)
        self.ui.spin_ColCount.setValue(colCount)
    def getTableSize(self):
        rows = self.ui.spin_RwoCount.value()
        cols = self.ui.spin_ColCount.value()
        return rows,cols
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyDialogSize()
    form.show()
    sys.exit(app.exec_())