import sys,os
from PyQt5.QtWidgets import QApplication,QWidget,QToolBar,QVBoxLayout,QFileDialog,QFontDialog
from PyQt5.QtCore import Qt,pyqtSlot,pyqtSignal
from ui_QWFormDoc import Ui_Form

class QmyQWFormDoc(QWidget):
    docFileChanged = pyqtSignal(str)
    def __init__(self,parent=None):
        super(QmyQWFormDoc, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.__curFile=''
        self.__buildUI()#创建工具栏
    def __buildUI(self):
        self.myToolBar = QToolBar(self)
        self.myToolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.myToolBar.addActions([self.ui.actOpen,self.ui.actFont])
        self.myToolBar.addSeparator()
        self.myToolBar.addActions([self.ui.actCut, self.ui.actCopy,self.ui.actPaste,self.ui.actUndo
                                   ,self.ui.actRedo])
        self.ui.actCut.triggered.connect(self.ui.plainTextEdit.cut)
        self.ui.actCopy.triggered.connect(self.ui.plainTextEdit.copy)
        self.ui.actPaste.triggered.connect(self.ui.plainTextEdit.paste)
        self.ui.actUndo.triggered.connect(self.ui.plainTextEdit.undo)
        self.ui.actRedo.triggered.connect(self.ui.plainTextEdit.redo)
        self.myToolBar.addSeparator()
        self.myToolBar.addAction(self.ui.actClose)
        layout = QVBoxLayout()
        layout.addWidget(self.myToolBar)
        layout.addWidget(self.ui.plainTextEdit)
        layout.setContentsMargins(2,2,2,2)#减少与四周的边距
        layout.setSpacing(2)#减少布局里组件之间的距离
        self.ui.actClose.triggered.connect(self.close)
        self.setLayout(layout)
    #打开文件
    @pyqtSlot()
    def on_actOpen_triggered(self):
        curPath = os.getcwd()
        filename,flt = QFileDialog.getOpenFileName(self,'打开文件',curPath,'文本文件(*.doc *.h *.py *.txt);;所有文件(*.*)')
        if filename =='':
            return
        self.__curFile=filename
        self.ui.plainTextEdit.clear()
        with open(filename,'r',encoding='utf-8') as f:
            for eachLine in f:
                self.ui.plainTextEdit.appendPlainText(eachLine.strip())
        baseFilename = os.path.basename(filename)#取得文件名称
        self.setWindowTitle(baseFilename)#将程序标题修改为文件名称
        self.docFileChanged.emit(baseFilename)#发射文件名信号
    #修改字体
    @pyqtSlot()
    def on_actFont_triggered(self):
        iniFont = self.ui.plainTextEdit.font()
        font,OK = QFontDialog.getFont(iniFont,self,'选择字体')
        if OK:
            self.ui.plainTextEdit.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyQWFormDoc()
    form.show()
    sys.exit(app.exec_())