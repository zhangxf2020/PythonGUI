import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5.QtCore import pyqtSignal,pyqtSlot
from ui_QWDialoglocate import Ui_QWDialogLocate
class QmyDialogLocate(QDialog):
    changeActionEnable = pyqtSignal(bool)
    changeCellText = pyqtSignal(int,int,str)
    def __init__(self,parent=None):
        super(QmyDialogLocate, self).__init__(parent)
        self.ui = Ui_QWDialogLocate()
        self.ui.setupUi(self)
        self.setRanges(20,50)
    def __del__(self):
        print('Qdialog被销毁了')
    def setRanges(self,row,col):
        self.ui.spinRow.setMaximum(row)
        self.ui.spinColumn.setMaximum(col)
    def do_setSpinValue(self,rowNo,colNo):
        self.ui.spinRow.setValue(rowNo)
        self.ui.spinColumn.setValue(colNo)
    @pyqtSlot()
    def on_btnSetText_clicked(self):
        row = self.ui.spinRow.value()
        col = self.ui.spinColumn.value()
        text = self.ui.editCellText.text()

        self.changeCellText.emit(row,col,text)
        if self.ui.chkBoxRow.isChecked():
            self.ui.spinRow.setValue(1+row)
        if self.ui.chkBoxColumn.isChecked():
            self.ui.spinColumn.setValue(1+col)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyDialogLocate()
    form.show()
    sys.exit(app.exec_())