from PyQt5.QtWidgets import QApplication,QMainWindow,QAbstractItemView,QFileDialog,QLabel
from PyQt5.QtCore import Qt,pyqtSlot,QItemSelectionModel,QDir,QModelIndex
from PyQt5.QtGui import QStandardItemModel,QStandardItem
import sys,os
from ui_MainWindow import Ui_MainWindow

class QmyMainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(QmyMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__ColCount = 6#常数,列数=6
        self.itemModel = QStandardItemModel(5,self.__ColCount,self) #定义类型模型,标准类型,5行 6列
        self.selectionModel = QItemSelectionModel(self.itemModel) #定义选择模型,与数据模型关联
        self.selectionModel.currentChanged[QModelIndex,QModelIndex].connect(self.do_curChanged)#选择模型的点击信号
        self.__lastColumnTitle = '测井取样' #最后一列文字
        self.__lastColumnFlags = (Qt.ItemIsSelectable | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled) #最后一列数据标志



        self.ui.tableView.setModel(self.itemModel) #table视图设置数据模型
        self.ui.tableView.setSelectionModel(self.selectionModel)#table视图设置选择模型
        self.ui.tableView.setSelectionMode(QAbstractItemView.ExtendedSelection)#table视图设置选择类型
        self.ui.tableView.setSelectionBehavior(QAbstractItemView.SelectItems) #table,项选择模式,单元格选择
        self.ui.tableView.verticalHeader().setDefaultSectionSize(22)#设置选择垂直标题字体大小
        self.ui.tableView.setAlternatingRowColors(True)#打开交替行颜色
        self.ui.tableView.setEnabled(False) #先禁用



        self.__buildStatusBar()

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~自定义功能函数~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __buildStatusBar(self):#状态栏显示信息
        self.LabCellPos = QLabel('当前单元格',self)
        self.LabCellPos.setMinimumWidth(180)
        self.ui.statusbar.addWidget(self.LabCellPos)

        self.LabCellText = QLabel('单元格内容',self)
        self.LabCellText.setMinimumWidth(150)
        self.ui.statusbar.addWidget(self.LabCellText)

        self.LabCurFile = QLabel('当前文件',self)
        self.ui.statusbar.addPermanentWidget(self.LabCurFile)
    def __iniModelFromStringList(self,allLines):#从字符串列表构建模型
        rowCnt = len(allLines)
        self.itemModel.setRowCount(rowCnt -1)#实际数据要比得到的行数少1,因为第一行是表头
        headerText = allLines[0].strip()#取出第一行数据
        headerList = headerText.split('\t')#生成表头字符串列表
        self.itemModel.setHorizontalHeaderLabels(headerList) #设置表头
        self.__lastColumnTitle = headerList[-1]#最后一列的表头字符串

        lastColNo = self.__ColCount -1
        for i in range(rowCnt -1):
            lineText = allLines[i+1].strip() #去除去掉多余字符的字符串,从第1行开始取
            strList = lineText.split('\t') #再将每一行转化为字符串列表
            for j,k in enumerate(strList): #循环字符串列表
                if j ==self.__ColCount -1: #如果是最后一列
                    item = QStandardItem(self.__lastColumnTitle)
                    item.setFlags(self.__lastColumnFlags)
                    item.setCheckable(True)
                    if k =='0':  #如果值为0,则设置勾选为false
                        item.setCheckState(Qt.Unchecked)
                    else:
                        item.setCheckState(Qt.Checked)
                else:
                    item =QStandardItem(k)
                self.itemModel.setItem(i,j,item)

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~自定义槽函数~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def do_curChanged(self,current,previous:QModelIndex):
        if current !=None:
            text = '当前单元格: {} 行, {} 列'.format(current.row(),current.column())
            self.LabCellPos.setText(text)
            item = self.itemModel.itemFromIndex(current)#从模型索引获取item
            self.LabCellText.setText('单元格内容: {}'.format(item.text()))
            font = item.font()
            self.ui.act_FontBold.setChecked(font.bold())
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~自动生成的函数~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    @pyqtSlot()
    def on_act_openFile_triggered(self): #打开文件
        curPath = os.getcwd()#返回程序所在路径
        filename,flt = QFileDialog.getOpenFileName(self,'打开一个文件',curPath,'井斜数据文件(*.txt);;所有文件(*.*)')#打开文件对话窗,返回文件名称路径和筛选标记
        if filename ==None:return
        self.LabCurFile.setText('当前文件: {}'.format(filename))
        with open(filename,'r') as f:
            allLines = f.readlines()
        for strLine in allLines:
            self.ui.plainTextEdit.appendPlainText(strLine.strip())#strip()取出字符串头尾字符,没有参数可去除空格/制表符/回车符
        self.__iniModelFromStringList(allLines)
        self.ui.tableView.setEnabled(True)
        self.ui.act_AddItem.setEnabled(True)
        self.ui.act_InsterItem.setEnabled(True)
        self.ui.act_DelItem.setEnabled(True)
        self.ui.act_SaveFile.setEnabled(True)
        self.ui.act_ModelData.setEnabled(True)
    @pyqtSlot()
    def on_act_AddItem_triggered(self):#添加行
        itemlist =[]
        for i in range(self.__ColCount):
            if i ==self.__ColCount -1:
                item = QStandardItem(self.__lastColumnTitle)
                item.setCheckable(True)  #需要放在上面
                item.setFlags(self.__lastColumnFlags)
            else:
                item = QStandardItem('0')
            itemlist.append(item)
        self.itemModel.appendRow(itemlist) #添加行,参数是一个Qstandarditem对象列表
        curIndex = self.itemModel.index(self.itemModel.rowCount() -1,0)
        self.selectionModel.clearSelection() #清除当前选择
        self.selectionModel.setCurrentIndex(curIndex,QItemSelectionModel.Select)#设置选择单元格,选择类型





if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyMainWindow()
    form.show()
    sys.exit(app.exec_())
        