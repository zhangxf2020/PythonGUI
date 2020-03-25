from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QProgressBar,QActionGroup,QSpinBox,\
    QFontComboBox
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QFont
import sys

from ui_MainWindow import Ui_MainWindow

class QmyMainWindow(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__buildUI()

    def __buildUI(self):
        self.__labFile = QLabel(self)
        self.__labFile.setMinimumWidth(150)
        self.__labFile.setText('文件名:')
        self.ui.statusbar.addWidget(self.__labFile)

        self.__progressBar1 = QProgressBar(self)
        self.__progressBar1.setMaximumWidth(200)
        self.__progressBar1.setRange(5,50)
        sz = self.ui.plainTextEdit.font().pointSize()
        self.__progressBar1.setValue(sz)
        self.ui.statusbar.addWidget(self.__progressBar1)

        self.__LabInfo = QLabel(self)
        self.__LabInfo.setText('选择字体名称:')
        self.ui.statusbar.addPermanentWidget(self.__LabInfo)

        actionGroup = QActionGroup(self)
        actionGroup.addAction(self.ui.actLang_CN)
        actionGroup.addAction(self.ui.actLang_EN)
        actionGroup.setExclusive(True)
        self.ui.actLang_CN.setChecked(True)

        self.__spinFontSize = QSpinBox(self)
        self.__spinFontSize.setRange(5,50)
        sz = self.ui.plainTextEdit.font().pointSize()
        self.__spinFontSize.setValue(sz)
        self.__spinFontSize.setMinimumWidth(50)
        self.ui.toolBar.addWidget(self.__spinFontSize)

        self.__comboFontName = QFontComboBox(self)
        self.__comboFontName.setMinimumWidth(100)
        self.ui.toolBar.addWidget(self.__comboFontName)

        self.ui.toolBar.addSeparator()
        self.ui.toolBar.addAction(self.ui.actClose)

    @pyqtSlot(bool)
    def on_actFont_Bold_triggered(self,checked):
        fmt = self.ui.plainTextEdit.currentCharFormat()
        if checked:
            fmt.setFontWeight(QFont.Bold)
        else:
            fmt.setFontWeight(QFont.Normal)
        self.ui.plainTextEdit.mergeCurrentCharFormat(fmt)

    @pyqtSlot(bool)
    def on_actFont_Italic_triggered(self,checked):
        fmt = self.ui.plainTextEdit.currentCharFormat()
        fmt.setFontItalic(checked)
        self.ui.plainTextEdit.mergeCurrentCharFormat(fmt)
    @pyqtSlot(bool)
    def on_actFont_UnderLine_triggered(self,checked):
        fmt = self.ui.plainTextEdit.currentCharFormat()
        fmt.setFontUnderline(checked)
        self.ui.plainTextEdit.mergeCurrentCharFormat(fmt)
    def on_plainTextEdit_copyAvailable(self,avi):
        self.ui.actEdit_Cut.setEnabled(avi)
        self.ui.actEdit_Copy.setEnabled(avi)
        self.ui.actEdit_Paste.setEnabled(self.ui.plainTextEdit.canPaste())
        print(self.ui.plainTextEdit.canPaste())
    def on_plainTextEdit_selectionChanged(self):
        fmt = self.ui.plainTextEdit.currentCharFormat()
        self.ui.actFont_Bold.setChecked(fmt.font().bold())
        self.ui.actFont_Italic.setChecked(fmt.fontItalic())
        self.ui.actFont_UnderLine.setChecked(fmt.fontUnderline())
    def on_plainTextEdit_customContextMenuRequested(self,pos):
        # popMenu = self.ui.plainTextEdit.createStandardContextMenu()
        # popMenu.exec(pos)
        print('youjian')


    @pyqtSlot(bool)
    def on_plainTextEdit_undoAvailable(self,avi):
        self.ui.actEdit_Undo.setEnabled(avi)

    def on_plainTextEdit_redoAvailable(self,avi):
        self.ui.actEdit_Redo.setEnabled(avi)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyMainWindow()
    form.show()
    sys.exit(app.exec_())