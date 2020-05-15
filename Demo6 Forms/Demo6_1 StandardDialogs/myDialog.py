from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog,QColorDialog,QProgressDialog,QFontDialog\
    ,QInputDialog,QLineEdit,QMessageBox

from PyQt5.QtGui import QPalette
from PyQt5.QtCore import pyqtSlot, QDir,Qt,QTime
import sys
from ui_Dialog import Ui_Dialog


class QmyDialog(QDialog):
    def __init__(self, parent=None):
        super(QmyDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.filt = "所有文件(*.*);;文本文件(*.txt);;图片文件(*.jpg *.gif *.png)"

    @pyqtSlot()
    def on_btn_Open_clicked(self): #选择文件
        curPath = QDir.currentPath()
        filename, filtUsed = QFileDialog.getOpenFileName(self, '选择一个文件', curPath, '所有文件(*.*);;文本' \
                                                                                  '文件(*.txt);;图片文件(*.jpg *.gif *.png *.bmp)')
        self.ui.plainTextEdit.appendPlainText(filename)
        self.ui.plainTextEdit.appendPlainText('\n' + filtUsed)
    @pyqtSlot()
    def on_btn_OpenMultipleFiles_clicked(self):#选择所有文件
        curPath = QDir.currentPath()
        fileList,filtUsed = QFileDialog.getOpenFileNames(self,'选择一个文件',curPath,'所有文件(*.*);;文本文件(*.txt);;图片文件'
                                                                  '(*.jpg *.gif *.png *.bmp)')
        for i in fileList:
            self.ui.plainTextEdit.appendPlainText(i)
        self.ui.plainTextEdit.appendPlainText('\n'+filtUsed)
    @pyqtSlot()
    def on_btn_ChooseExistiongDirectory_clicked(self):#选择已有目录
        curPath = QDir.currentPath()
        selectedDir = QFileDialog.getExistingDirectory(self,'选择一个目录',curPath,QFileDialog.ShowDirsOnly)
        self.ui.plainTextEdit.appendPlainText('\n'+selectedDir)
    @pyqtSlot()
    def on_btn_Save_clicked(self):#保存文件
        curPath = QDir.currentPath()
        filename,filtUsed = QFileDialog.getSaveFileName(self,'保存文件',curPath,self.filt)
        self.ui.plainTextEdit.appendPlainText(filename)
        self.ui.plainTextEdit.appendPlainText('\n'+filtUsed)
    @pyqtSlot()
    def on_btn_ChooseColor_clicked(self):#选择颜色
        pal = self.ui.plainTextEdit.palette() #取得对象的调色板
        iniColor = pal.color(QPalette.Text) #取得对应位置的颜色对象(这里是前景色)
        color = QColorDialog.getColor(iniColor,self,'选择颜色')#打开取色对话窗,并返回所得的颜色对象
        if color.isValid(): #判断颜色是否合法,或是是否点击了取色
            pal.setColor(QPalette.Text,color)
            self.ui.plainTextEdit.setPalette(pal)
    @pyqtSlot()
    def on_btn_ChooseFont_clicked(self):#选择字体
        iniFont = self.ui.plainTextEdit.font()
        font,OK = QFontDialog.getFont(iniFont)
        if OK:
            self.ui.plainTextEdit.setFont(font)
    @pyqtSlot()
    def on_btn_ProgressDialog_clicked(self):
        dlgProgess = QProgressDialog('正在复制文件','取消',0,200,self)#设置进度条文本显示和值的范围
        dlgProgess.canceled.connect(self.do_progress_canceled)#点击取消按钮后发射信号

        dlgProgess.setWindowTitle('复制文件')
        dlgProgess.setWindowModality(Qt.WindowModal)#开启模态(阻塞其他窗口,目的是为了当前聚焦点)

        dlgProgess.setAutoReset(True)#进度是否达到上限后重头
        dlgProgess.setAutoClose(True)#一旦重头是否隐藏面板进

        msCounter = QTime()
        for i in range(0,200+1):
            dlgProgess.setValue(i)
            dlgProgess.setLabelText('正在复制文件,第{}个'.format(i))
            msCounter.start()#保存当前执行时间
            while msCounter.elapsed() <30:#如果与上一次start()之间小于30毫秒,就循环,循环体内什么都不做,相当于流逝30毫秒
                None
            if dlgProgess.wasCanceled():#如果取消了对话窗,则跳出循环
                break
    def do_progress_canceled(self):
        self.ui.plainTextEdit.appendPlainText('进度对话框被取消了**')
    ##字符串对话框
    @pyqtSlot()
    def on_btn_InputString_clicked(self):
        ##参数(父对象,标题,窗口文本,显示模式(普通,密码等),输入框默认显示内容);返回输入文本和点击的按钮
        text,OK = QInputDialog.getText(self,'输入文字对话框','请输入文件名',QLineEdit.Normal,'新建文件.txt')
        if OK:
            self.ui.plainTextEdit.appendPlainText(text)
    #输入整数对话框
    @pyqtSlot()
    def on_btn_EnterInteger_clicked(self):
        # 参数(父对象,标题,窗口文本,当前值,最小值,最大值,步长;返回输入的整数和点击的按钮
        inputValue,OK = QInputDialog.getInt(self,'输入整数对话框','设置字体大小',self.ui.plainTextEdit.font().pointSize()
                                            ,6,50,1)
        if OK:
            font = self.ui.plainTextEdit.font()
            font.setPointSize(inputValue)
            self.ui.plainTextEdit.setFont(font)
    #输入浮点数
    @pyqtSlot()
    def on_btn_EnterFloat_clicked(self):
        # 参数(父对象,标题,窗口文本,当前值,最小值,最大值,小数点位数;返回输入的整数和点击的按钮
        inputValue,OK = QInputDialog.getDouble(self,'输入浮点数对话框','输入一个浮点数',3.65,0,10000,2)
        if OK:
            text = '输入了一个浮点数:{:.1f}'.format(inputValue)
            self.ui.plainTextEdit.appendPlainText(text)
    #条目选择输入
    @pyqtSlot()
    def on_btn_EntrySelectionInput_clicked(self):
        items = ['优秀','良好','合格','不合格']
        # 参数(父对象,标题,窗口文本,选择内容(一个列表),当前选项index,输入模式(可输入,不可输入));返回输入的内容和点击的按钮
        text,OK = QInputDialog.getItem(self,'条目选择对话框','请选择级别',items,0,True)
        if OK:
            self.ui.plainTextEdit.appendPlainText(text)
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~我是分割线~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #询问窗口(一般选择性窗口)
    @pyqtSlot()
    def on_btn_MSGquestion_clicked(self):
        # 参数(父对象,标题,窗口文本,需要展示的组合按钮,缺省按钮(未选择前的按钮));返回点击的按钮
        result = QMessageBox.question(self,'问题窗口','文件已被修改,是否保存修改?',QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel,QMessageBox.NoButton)
        if result ==QMessageBox.Yes:
            self.ui.plainTextEdit.appendPlainText('question消息框:Yes 被选择')
        elif result == QMessageBox.No:
            self.ui.plainTextEdit.appendPlainText('question消息框:No 被选择')
        elif result == QMessageBox.Cancel:
            self.ui.plainTextEdit.appendPlainText('question消息框:Cancel 被选择')
        else:
            self.ui.plainTextEdit.appendPlainText('question消息框:无选择')
    #信息窗口(帮助信息的窗口)
    @pyqtSlot()
    def on_btn_MSGinformation_clicked(self):
        # 参数(父对象,标题,窗口文本,需要展示的组合按钮(不填写默认有一个OK),缺省按钮(未选择前的按钮));返回点击的按钮
        result = QMessageBox.information(self,'信息窗口','文件已经被正常打开')
    #警告窗口(危险操作的提示)
    @pyqtSlot()
    # 参数(父对象,标题,窗口文本,需要展示的组合按钮(不填写默认有一个OK),缺省按钮(未选择前的按钮));返回点击的按钮
    def on_btn_MSGwarning_clicked(self):
        result = QMessageBox.warning(self,'warning消息框','文件内容已经被修改')
    #关键提示(出现错误的提示)
    @pyqtSlot()
    def on_btn_MSGcritical_clicked(self):
        result = QMessageBox.critical(self,'critical消息框','出现严重错误,即将关闭')
    #关于提示
    @pyqtSlot()
    def on_btn_MSGabout_clicked(self):
        result = QMessageBox.about(self,'关于','Python Qt GUI与数据可视化编程\n保留所有版权')
    #关于Qt窗口
    @pyqtSlot()
    def on_btn_MSGaboutQt_clicked(self):
        #参数(父对象,标题)直接弹出Qt的关于窗口
        result = QMessageBox.aboutQt(self,'关于Qt')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyDialog()
    form.show()
    sys.exit(app.exec_())
