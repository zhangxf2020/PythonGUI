from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import pyqtSlot,Qt
from PyQt5.QtGui import QFont,QIcon
import sys,inspect

from ui_Widget import Ui_Widget

class QmyWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(r':/icons/images/app.ico'))

    @pyqtSlot(bool)
    def on_btnAlign_Left_clicked(self,checked):
        if checked:
            self.ui.editInput.setAlignment(Qt.AlignLeft)
    @pyqtSlot(bool)
    def on_btnAlign_Right_clicked(self,checked):
        if checked:
            self.ui.editInput.setAlignment(Qt.AlignRight)
    def on_btnAlign_Center_clicked(self):
        self.ui.editInput.setAlignment(Qt.AlignCenter)
    @pyqtSlot(bool)
    def on_btnFont_Bold_clicked(self,checked):
        font = self.ui.editInput.font()
        font.setBold(checked)
        self.ui.editInput.setFont(font)
    @pyqtSlot(bool)
    def on_btnFont_Italic_clicked(self,checked):
        font = self.ui.editInput.font()
        font.setItalic(checked)
        self.ui.editInput.setFont(font)
    @pyqtSlot(bool)
    def on_btnFont_UnderLine_clicked(self,checked):
        font = self.ui.editInput.font()
        font.setUnderline(checked)
        self.ui.editInput.setFont(font)

    @pyqtSlot(bool)
    def on_checkBox_Enabled_clicked(self,checked):
        self.ui.editInput.setEnabled(checked)

    @pyqtSlot(bool)
    def on_chkBox_Readonly_clicked(self, checked):
        self.ui.editInput.setReadOnly(checked)

    @pyqtSlot(bool)
    def on_check_ClearButton_clicked(self, checked):
        self.ui.editInput.setClearButtonEnabled(checked)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())