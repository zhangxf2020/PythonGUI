from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QTableWidgetItem,QAbstractItemView
from PyQt5.QtCore import pyqtSlot,Qt,QDate
from PyQt5.QtGui import QBrush,QIcon
import sys
from enum import Enum
from ui_MainWindow import Ui_MainWindow

class CellType(Enum): #各个单元格的枚举类型
    ctName = 1000
    ctSex = 1001
    ctBirth = 1002
    ctNation = 1003
    ctScore = 1004
    ctPartyM = 1005

class FieldColNum(Enum): #各个字段在表格中的列号
    colName = 0
    colSex = 1
    colBirth = 2
    colNation = 3
    colScore = 4
    colPartyM = 5

class QmyMainWindow(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.LabCellIndex = QLabel('当前单元格坐标:',self)
        self.LabCellIndex.setMinimumWidth(250)
        self.LabCellType = QLabel('当前单元格类型:',self)
        self.LabCellType.setMinimumWidth(200)
        self.LabStudID = QLabel('学生ID:',self)
        self.LabStudID.setMinimumWidth(200)
        self.ui.statusbar.addWidget(self.LabCellIndex)
        self.ui.statusbar.addWidget(self.LabCellType)
        self.ui.statusbar.addWidget(self.LabStudID)

        self.__stuIDNum = 20200401 #创建一个学号私有变量用以累加
        self.ui.tableinfo.setAlternatingRowColors(True)
        self.__tableInitialized = False

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~自动生成的函数~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #设置表头列数/内容/格式
    @pyqtSlot()
    def on_btn_setHeader_clicked(self):
        headerText = ["姓 名","性 别","出生日期","民 族","分数","是否党员"]
        self.ui.tableinfo.setColumnCount(len(headerText))#设置表头列数
        for i in range(len(headerText)):
            headerItem = QTableWidgetItem(headerText[i])#创建QtabWidgetitem,参数为表头内容
            font = headerItem.font() #设置字体颜色和字体大小
            font.setPointSize(11)
            headerItem.setFont(font)
            headerItem.setForeground(QBrush(Qt.red))
            self.ui.tableinfo.setHorizontalHeaderItem(i,headerItem)#生成表头
    #设置行数
    @pyqtSlot()
    def on_btn_setRows_clicked(self):
        self.ui.tableinfo.setRowCount(self.ui.spinBox_Row.value()) #设置行数
        self.ui.tableinfo.setAlternatingRowColors(self.ui.chbox_RowBackground.isChecked())#设置根据勾选框打开关闭间隔行底色
    #初始化表格数据
    @pyqtSlot()
    def on_btn_IniTabularData_clicked(self):
        self.__stuIDNum = 20200401 #点击了初始化,学号重新计算
        self.ui.tableinfo.clearContents()#此清理代表只清理表格内容,不清理表头和列标题
        birth = QDate(1988,6,23) #创建日期对象,作为学生的生日
        isParty = True #作为是否党员的凭证
        nation = '汉族'
        score = 70

        rowCount = self.ui.tableinfo.rowCount() #获得总行数
        for i in range(rowCount):
            strName = '学生{}'.format(i)
            if i % 2 ==0:
                strSex = '男'
            else:
                strSex = '女'
            self.__createItemsARow(i,strName,strSex,birth,nation,isParty,score)
            birth = birth.addDays(20) #每循环一次生日加20天
            isParty = not isParty #每循环一次,党员取反
        self.__tableInitialized = True #初始化变为真(表明已经初始化)
    #插入行
    @pyqtSlot()
    def on_btn_InsertRow_clicked(self):
        curRow = self.ui.tableinfo.currentRow()
        if curRow < 0:
            curRow = 0
        self.ui.tableinfo.insertRow(curRow)
        birth = QDate.fromString('1999-1-10','yyyy-M-d')
        self.__createItemsARow(curRow,'新学生','女',birth,'蒙古族',True,68)
    #添加行
    @pyqtSlot()
    def on_btn_AddRow_clicked(self):
        rowCount = self.ui.tableinfo.rowCount()
        self.ui.tableinfo.insertRow(rowCount)
        birth = QDate.fromString('1989-12-10','yyyy-M-d')
        self.__createItemsARow(rowCount,'新生','男',birth,'维吾尔族',False,50)
    #删除行
    @pyqtSlot()
    def on_btn_DelCurrentRow_clicked(self):
        curRow = self.ui.tableinfo.currentRow()
        self.ui.tableinfo.removeRow(curRow)
    #清空表格内容
    @pyqtSlot()
    def on_btn_ClearContents_clicked(self):
        self.ui.tableinfo.clearContents()
    #自动调节行高
    @pyqtSlot()
    def on_btn_AutoRowHeight_clicked(self):
        self.ui.tableinfo.resizeRowsToContents()
    # 自动调节列宽
    @pyqtSlot()
    def on_btn_AutoRowWidth_clicked(self):
        self.ui.tableinfo.resizeColumnsToContents()
    #读取表格到文本
    @pyqtSlot()
    def on_btn_ReadIntoText_clicked(self):
        self.ui.textEdit.clear()
        rowCount = self.ui.tableinfo.rowCount()
        colCount = self.ui.tableinfo.columnCount()
        for i in range(rowCount):
            strText = '第{}行:  '.format(i+1)
            for j in range(colCount-1): #因为最后一列需要判断,所以这里只取到倒数第2列
                cellItem = self.ui.tableinfo.item(i,j) #按顺序取出每行的单元格item
                strText += cellItem.text() +'  '
            cellItem = self.ui.tableinfo.item(i,colCount-1) #最后一列单元格单独处理
            if cellItem.checkState() ==Qt.Checked: #判断是否选中,选中的为党员,非选中的为群众
                strText += '党员'
            else:
                strText += '群众'
            font = self.ui.textEdit.font()
            font.setBold(True)
            font.setPointSize(12)
            font.setFamily('隶书')
            self.ui.textEdit.setFont(font)
            self.ui.textEdit.setStyleSheet(r'color:blue')
            self.ui.textEdit.appendPlainText(strText)
    #表格可编辑
    @pyqtSlot(bool)
    def on_chbox_TableCanEdited_toggled(self,checked):
        #判断表格可编辑是否勾选,是的话可编辑,不是则不可编辑
        self.ui.tableinfo.setEditTriggers(QAbstractItemView.DoubleClicked | QAbstractItemView.SelectedClicked if checked else QAbstractItemView.NoEditTriggers)
    #是否添加间隔色
    @pyqtSlot(bool)
    def on_chbox_RowBackground_toggled(self,checked):
        self.ui.tableinfo.setAlternatingRowColors(checked)
    #是否显示行表头
    @pyqtSlot(bool)
    def on_chbox_ShowRowHeader_toggled(self,checked):
        self.ui.tableinfo.horizontalHeader().setVisible(checked)
    #是否显示列表头
    @pyqtSlot(bool)
    def on_chbox_ShowListHeader_toggled(self,checked):
        self.ui.tableinfo.verticalHeader().setVisible(checked)
    #行选择/列选择,因为有互斥,所以判断一个单选框的结果就可以了
    @pyqtSlot(bool)
    def on_radionbtn_RowSelection_toggled(self,checked):
        if checked:
            self.ui.tableinfo.setSelectionBehavior(QAbstractItemView.SelectRows)
        else:
            self.ui.tableinfo.setSelectionBehavior(QAbstractItemView.SelectItems)
    #点击单元格时触发信号,写入状态栏

    @pyqtSlot(int,int,int,int)
    def on_tableinfo_currentCellChanged(self,currentRow,currentCol,previousRow,previousCol):
        if self.__tableInitialized == False:
            return
        curItem = self.ui.tableinfo.item(currentRow,currentCol)
        if curItem ==None:
            return
        self.LabCellIndex.setText('当前单元格坐标: {}行  {}列'.format(currentRow,currentCol))
        self.LabCellType.setText('单元格类型: {}'.format(curItem.type()))
        curItem2 = self.ui.tableinfo.item(currentRow,FieldColNum.colName.value)
        stuID = curItem2.data(Qt.UserRole)
        self.LabStudID.setText('学生ID: {}'.format(stuID))








##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~自定义函数~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __createItemsARow(self,rowNo,name,sex,birth,nation,isParty,score):
        self.__stuIDNum +=1 #每调用一次此函数,学号+1,不论是插入还是添加还是初始化
        #初始化---添加姓名列
        item = QTableWidgetItem(name,CellType.ctName.value)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font = item.font()
        font.setBold(True)
        item.setFont(font)
        item.setData(Qt.UserRole,self.__stuIDNum) #给item设置个人标志,主要保存学号
        self.ui.tableinfo.setItem(rowNo,FieldColNum.colName.value,item)

        # 初始化---添加性别列
        item = QTableWidgetItem(sex,CellType.ctSex.value)
        if sex == '男':
            icon = QIcon(r":/icons/images/boy.ico")
        else:
            icon = QIcon(r":/icons/images/girl.ico")
        item.setIcon(icon)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.ui.tableinfo.setItem(rowNo,FieldColNum.colSex.value,item)
        #初始化---添加出生日期列
        strBirth = birth.toString('yyyy-MM-dd')
        item = QTableWidgetItem(strBirth,CellType.ctBirth.value)
        item.setTextAlignment(Qt.AlignVCenter|Qt.AlignHCenter)
        self.ui.tableinfo.setItem(rowNo,FieldColNum.colBirth.value,item)
        #初始化---民族列
        item = QTableWidgetItem(nation,CellType.ctNation.value)
        if nation !='汉族':
            item.setForeground(QBrush(Qt.blue))
        item.setTextAlignment(Qt.AlignCenter)
        self.ui.tableinfo.setItem(rowNo,FieldColNum.colNation.value,item)
        #初始化---分数列
        item = QTableWidgetItem(str(score),CellType.ctScore.value)
        item.setTextAlignment(Qt.AlignCenter)
        self.ui.tableinfo.setItem(rowNo,FieldColNum.colScore.value,item)
        #初始化---党员列
        item = QTableWidgetItem('党员',CellType.ctPartyM.value)
        item.setTextAlignment(Qt.AlignCenter)
        if isParty:
            item.setCheckState(Qt.Checked)
        else:
            item.setCheckState(Qt.Unchecked)
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)

        item.setBackground(QBrush(Qt.yellow))
        self.ui.tableinfo.setItem(rowNo,FieldColNum.colPartyM.value,item)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyMainWindow()
    form.show()
    sys.exit(app.exec_())