from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.QtCore import pyqtSlot
from ui_Dialog import Ui_Dialog
import sys

class QmyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.radioRed.toggled.connect(self.do_setTextColor)
        self.ui.radioBlue.toggled.connect(self.do_setTextColor)
        self.ui.radioBlack.toggled.connect(self.do_setTextColor)
    def on_btnClear_clicked(self):
        self.ui.textEdit.clear()
    def on_chkBoxUnder_toggled(self,checked):
        font = self.ui.textEdit.font()
        font.setUnderline(checked)
        self.ui.textEdit.setFont(font)
        self.ui.chkBoxItalic
    def on_chkBoxItalic_toggled(self,checked):
        font = self.ui.textEdit.font()
        font.setItalic(checked)
        self.ui.textEdit.setFont(font)

    '''chilkbox默认clicked信号是不带参数的，像这样传递参数后需要添加修饰符'''
    @pyqtSlot(bool)
    def on_chkBoxBold_clicked(self,checked):
        font = self.ui.textEdit.font()
        font.setBold(checked)
        self.ui.textEdit.setFont(font)
    def do_setTextColor(self):
        if self.ui.radioBlack.isChecked():
            self.ui.textEdit.setStyleSheet('color:black')
        elif self.ui.radioBlue.isChecked():
            self.ui.textEdit.setStyleSheet('color:blue')
        elif self.ui.radioRed.isChecked():
            self.ui.textEdit.setStyleSheet('color:red')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyDialog()
    form.show()
    sys.exit(app.exec_())