from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QProgressBar,QActionGroup,QSpinBox,\
    QFontComboBox
from PyQt5.QtCore import pyqtSlot,Qt
from PyQt5.QtGui import QFont
import sys

from ui_MainWindow import Ui_MainWindow

class QmyMainWindow(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__buildUI()
        self.setCentralWidget(self.ui.plainTextEdit)#设置plaintextedit为中心窗口,这样就可以铺满整个界面
        self.__spinFontSize.valueChanged[int].connect(self.do_fontSize_Changed)#将字体调节按钮关联至自定义函数
        self.__comboFontName.currentIndexChanged[str].connect(self.do_fontName_Changed)#将字体家族下拉框关联自定义函数

    def __buildUI(self):#自定义函数,构造函数中直接调用,初始化状态栏中按钮
        #创建一个标签,并添加至状态栏
        self.__labFile = QLabel(self)
        self.__labFile.setMinimumWidth(150)
        self.__labFile.setText('文件名:')
        self.ui.statusbar.addWidget(self.__labFile)

        #创建一个进度条,添加至状态栏
        self.__progressBar1 = QProgressBar(self)
        self.__progressBar1.setMaximumWidth(200)
        self.__progressBar1.setRange(5,50)
        sz = self.ui.plainTextEdit.font().pointSize()#获得plaintextEdit中字体的尺寸
        self.__progressBar1.setValue(sz)
        self.ui.statusbar.addWidget(self.__progressBar1)

        #创建一个标签,添加至状态栏
        self.__LabInfo = QLabel(self)
        self.__LabInfo.setText('选择字体名称:')
        self.ui.statusbar.addPermanentWidget(self.__LabInfo)

        #创建一个行为分组,添加中/英行为按钮,并打开互斥
        actionGroup = QActionGroup(self)
        actionGroup.addAction(self.ui.actLang_CN)
        actionGroup.addAction(self.ui.actLang_EN)
        actionGroup.setExclusive(True)
        self.ui.actLang_CN.setChecked(True)

        #创建一个步长调节器,添加至工具栏,并根据当前文本字体尺寸来改变自身value值
        self.__spinFontSize = QSpinBox(self)
        self.__spinFontSize.setRange(5,50)
        sz = self.ui.plainTextEdit.font().pointSize()
        self.__spinFontSize.setValue(sz)
        self.__spinFontSize.setMinimumWidth(50)
        self.ui.toolBar.addWidget(self.__spinFontSize)

        #创建一个字体下拉选项框,将之添加到工具栏中
        self.__comboFontName = QFontComboBox(self)
        self.__comboFontName.setMinimumWidth(100)
        self.ui.toolBar.addWidget(self.__comboFontName)

        #添加一个竖线和一个关闭行为按钮
        self.ui.toolBar.addSeparator()
        self.ui.toolBar.addAction(self.ui.actClose)

    @pyqtSlot(bool)
    #点击字体加粗行为按钮时触发
    def on_actFont_Bold_triggered(self,checked):
        fmt = self.ui.plainTextEdit.currentCharFormat()
        if checked:
            fmt.setFontWeight(QFont.Bold)#注意设置粗体时使用的时FontWeight
        else:
            fmt.setFontWeight(QFont.Normal)
        self.ui.plainTextEdit.mergeCurrentCharFormat(fmt)

    @pyqtSlot(bool)
    #点击斜体行为按钮时触发
    def on_actFont_Italic_triggered(self,checked):
        fmt = self.ui.plainTextEdit.currentCharFormat()
        fmt.setFontItalic(checked)
        self.ui.plainTextEdit.mergeCurrentCharFormat(fmt)
    @pyqtSlot(bool)
    #点击下划线行为按钮时触发
    def on_actFont_UnderLine_triggered(self,checked):
        fmt = self.ui.plainTextEdit.currentCharFormat()
        fmt.setFontUnderline(checked)
        self.ui.plainTextEdit.mergeCurrentCharFormat(fmt)#设置当前选择字体格式
    #当plaintextedit可以复制时自动触发
    def on_plainTextEdit_copyAvailable(self,avi):
        self.ui.actEdit_Cut.setEnabled(avi)
        self.ui.actEdit_Copy.setEnabled(avi)
        self.ui.actEdit_Paste.setEnabled(self.ui.plainTextEdit.canPaste())
    #当plaintextedit有变动时自动触发
    def on_plainTextEdit_selectionChanged(self):
        fmt = self.ui.plainTextEdit.currentCharFormat()#获取选择字体格式
        self.ui.actFont_Bold.setChecked(fmt.font().bold())
        self.ui.actFont_Italic.setChecked(fmt.fontItalic())
        self.ui.actFont_UnderLine.setChecked(fmt.fontUnderline())
        self.__LabInfo.setText(fmt.fontFamily())
        # self.__spinFontSize.setValue(fmt.font().pointSize())

    #不知道啥意思
    def on_plainTextEdit_customContextMenuRequested(self,pos):
        popMenu = self.ui.plainTextEdit.createStandardContextMenu()
        popMenu.exec(pos)

    @pyqtSlot(bool)
    def on_actSys_ToggleText_triggered(self,checked):
        # 如果点击了按钮,就是一种样式,否则是另一种样式
        if checked:
            st = Qt.ToolButtonTextUnderIcon#行文按钮下方显示文字
        else:
            st = Qt.ToolButtonIconOnly#只显示图标
        self.ui.toolBar.setToolButtonStyle(st)


    @pyqtSlot(bool)
    #关联撤销操作,信号在可以撤销时触发
    def on_plainTextEdit_undoAvailable(self,avi):
        self.ui.actEdit_Undo.setEnabled(avi)

    # 关联重做操作,信号在可以重做时触发
    def on_plainTextEdit_redoAvailable(self,avi):
        self.ui.actEdit_Redo.setEnabled(avi)


    #自定义函数,当改变了字体尺寸时触发
    def do_fontSize_Changed(self,fontSize):
        font = self.ui.plainTextEdit.currentCharFormat()
        font.setFontPointSize(fontSize)
        self.ui.plainTextEdit.mergeCurrentCharFormat(font)
        self.__progressBar1.setValue(fontSize)
    #自定义函数,当改变字体家族时触发
    def do_fontName_Changed(self,fontName):
        font = self.ui.plainTextEdit.currentCharFormat()
        font.setFontFamily(fontName)
        self.ui.plainTextEdit.mergeCurrentCharFormat(font)
        self.__LabInfo.setText('字体名称:{}'.format(fontName))
    #以下当点击新建/打开/保存行为按钮时触发,无实际作用
    def on_actFile_New_triggered(self):
        self.__labFile.setText('新建文件')
    def on_actFile_Open_triggered(self):
        self.__labFile.setText('打开文件')
    def on_actFile_Save_triggered(self):
        self.__labFile.setText('文件已保存')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyMainWindow()
    form.show()
    sys.exit(app.exec_())