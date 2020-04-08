from PyQt5.QtWidgets import QApplication, QMainWindow, QAbstractItemView, QFileDialog, QLabel
from PyQt5.QtCore import Qt, pyqtSlot, QItemSelectionModel, QDir, QModelIndex
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import sys, os
from ui_MainWindow import Ui_MainWindow
from myDelegates import QmyComoBoxDelegate,QmyFloatSpinDelegate


class QmyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QmyMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__ColCount = 6  # 常数,列数=6
        self.itemModel = QStandardItemModel(5, self.__ColCount, self)  # 定义类型模型,标准类型,5行 6列
        self.selectionModel = QItemSelectionModel(self.itemModel)  # 定义选择模型,与数据模型关联
        self.selectionModel.currentChanged[QModelIndex, QModelIndex].connect(self.do_curChanged)  # 选择模型的点击信号
        self.__lastColumnTitle = '测井取样'  # 最后一列文字
        self.__lastColumnFlags = (Qt.ItemIsSelectable | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)  # 最后一列数据标志

        self.ui.tableView.setModel(self.itemModel)  # table视图设置数据模型
        self.ui.tableView.setSelectionModel(self.selectionModel)  # table视图设置选择模型
        self.ui.tableView.setSelectionMode(QAbstractItemView.ExtendedSelection)  # table视图设置选择类型
        self.ui.tableView.setSelectionBehavior(QAbstractItemView.SelectItems)  # table,项选择模式,单元格选择
        self.ui.tableView.verticalHeader().setDefaultSectionSize(22)  # 设置选择垂直标题字体大小
        self.ui.tableView.setAlternatingRowColors(True)  # 打开交替行颜色
        self.ui.tableView.setEnabled(False)  # 先禁用
        ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~创建自定义代理组件~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.spinCeShen = QmyFloatSpinDelegate(0,10000,0,self) #创建代理组件,分别设置不同的范围,和小数位数
        self.spinLength = QmyFloatSpinDelegate(0,6000,2,self)
        self.spinDegree = QmyFloatSpinDelegate(0,360,1,self)

        self.ui.tableView.setItemDelegateForColumn(0,self.spinCeShen)#将代理组件与视图关联(列,组件)
        self.ui.tableView.setItemDelegateForColumn(1,self.spinLength)
        self.ui.tableView.setItemDelegateForColumn(3,self.spinLength)
        self.ui.tableView.setItemDelegateForColumn(2,self.spinDegree)

        qualities = ['优','良','合格','不合格']
        self.comboDelegate = QmyComoBoxDelegate(self)
        self.comboDelegate.setItems(qualities,False)#设置组件列表和编辑与否
        self.ui.tableView.setItemDelegateForColumn(4,self.comboDelegate)

        self.__buildStatusBar()

    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~自定义功能函数~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __buildStatusBar(self):  # 状态栏显示信息
        self.LabCellPos = QLabel('当前单元格', self)
        self.LabCellPos.setMinimumWidth(180)
        self.ui.statusbar.addWidget(self.LabCellPos)

        self.LabCellText = QLabel('单元格内容', self)
        self.LabCellText.setMinimumWidth(150)
        self.ui.statusbar.addWidget(self.LabCellText)

        self.LabCurFile = QLabel('当前文件', self)
        self.ui.statusbar.addPermanentWidget(self.LabCurFile)

    def __iniModelFromStringList(self, allLines):  # 从字符串列表构建模型
        rowCnt = len(allLines)
        self.itemModel.setRowCount(rowCnt - 1)  # 实际数据要比得到的行数少1,因为第一行是表头
        headerText = allLines[0].strip()  # 取出第一行数据
        headerList = headerText.split('\t')  # 生成表头字符串列表
        self.itemModel.setHorizontalHeaderLabels(headerList)  # 设置表头
        self.__lastColumnTitle = headerList[-1]  # 最后一列的表头字符串

        lastColNo = self.__ColCount - 1
        for i in range(rowCnt - 1):
            lineText = allLines[i + 1].strip()  # 去除去掉多余字符的字符串,从第1行开始取
            strList = lineText.split('\t')  # 再将每一行转化为字符串列表
            for j, k in enumerate(strList):  # 循环字符串列表
                if j == self.__ColCount - 1:  # 如果是最后一列
                    item = QStandardItem(self.__lastColumnTitle)
                    item.setFlags(self.__lastColumnFlags)
                    item.setCheckable(True)
                    if k == '0':  # 如果值为0,则设置勾选为false
                        item.setCheckState(Qt.Unchecked)
                    else:
                        item.setCheckState(Qt.Checked)
                else:
                    item = QStandardItem(k)
                self.itemModel.setItem(i, j, item)

    def __setCellAlignment(self, align=Qt.AlignCenter):  # 单元格内容位置对其方式
        if not self.selectionModel.hasSelection():  # 如果没有选择的单元格就退出
            return
        selectedIndex = self.selectionModel.selectedIndexes()  # 得到所选择的单元格索引列表
        count = len(selectedIndex)
        for i in range(count):
            index = selectedIndex[i]
            item = self.itemModel.itemFromIndex(index)
            item.setTextAlignment(align)

    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~自定义槽函数~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def do_curChanged(self, current, previous: QModelIndex):
        if current != None:
            text = '当前单元格: {} 行, {} 列'.format(current.row(), current.column())
            self.LabCellPos.setText(text)
            item = self.itemModel.itemFromIndex(current)  # 从模型索引获取item
            self.LabCellText.setText('单元格内容: {}'.format(item.text()))
            font = item.font()
            self.ui.act_FontBold.setChecked(font.bold())

    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~自动生成的函数~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    @pyqtSlot()
    def on_act_openFile_triggered(self):  # 打开文件
        curPath = os.getcwd()  # 返回程序所在路径
        filename, flt = QFileDialog.getOpenFileName(self, '打开一个文件', curPath, '井斜数据文件(*.txt);;所有文件(*.*)')  # 打开文件对话窗,返回文件名称路径和筛选标记
        if filename == None: return
        self.LabCurFile.setText('当前文件: {}'.format(filename))
        with open(filename, 'r') as f:
            allLines = f.readlines()
        for strLine in allLines:
            self.ui.plainTextEdit.appendPlainText(strLine.strip())  # strip()取出字符串头尾字符,没有参数可去除空格/制表符/回车符
        self.__iniModelFromStringList(allLines)
        self.ui.tableView.setEnabled(True)
        self.ui.act_AddItem.setEnabled(True)
        self.ui.act_InsterItem.setEnabled(True)
        self.ui.act_DelItem.setEnabled(True)
        self.ui.act_SaveFile.setEnabled(True)
        self.ui.act_ModelData.setEnabled(True)

    @pyqtSlot()
    def on_act_AddItem_triggered(self):  # 添加行
        itemlist = []
        for i in range(self.__ColCount):
            if i == self.__ColCount - 1:
                item = QStandardItem(self.__lastColumnTitle)
                item.setCheckable(True)  # 需要放在上面
                item.setFlags(self.__lastColumnFlags)
            else:
                item = QStandardItem('0')
            itemlist.append(item)
        self.itemModel.appendRow(itemlist)  # 添加行,参数是一个Qstandarditem对象列表
        curIndex = self.itemModel.index(self.itemModel.rowCount() - 1, 0)
        self.selectionModel.clearSelection()  # 清除当前选择
        self.selectionModel.setCurrentIndex(curIndex, QItemSelectionModel.Select)  # 设置选择单元格,选择类型

    @pyqtSlot()
    def on_act_InsterItem_triggered(self):  # 插入行
        itemlist = []
        for i in range(self.__ColCount):
            if i == self.__ColCount - 1:
                item = QStandardItem(self.__lastColumnTitle)
                item.setCheckable(True)
                item.setFlags(self.__lastColumnFlags)
            else:
                item = QStandardItem('inster item')
            itemlist.append(item)
        curIndex = self.selectionModel.currentIndex()  # 返回所选择单元格的索引
        self.itemModel.insertRow(curIndex.row(), itemlist)  # 按照行插入单元格,如果行大于最大行数,则在最后添加
        self.selectionModel.clearSelection()
        self.selectionModel.setCurrentIndex(self.itemModel.index(curIndex.row(), 0), QItemSelectionModel.Select)

    @pyqtSlot()
    def on_act_DelItem_triggered(self):  # 删除行
        curIdex = self.selectionModel.currentIndex()
        self.itemModel.removeRow(curIdex.row())

    @pyqtSlot()
    def on_act_Left_triggered(self):  # 居左
        self.__setCellAlignment(Qt.AlignLeft | Qt.AlignVCenter)

    @pyqtSlot()
    def on_act_Center_triggered(self):  # 居中
        self.__setCellAlignment(Qt.AlignCenter)

    @pyqtSlot()
    def on_act_Right_triggered(self):  # 居右
        self.__setCellAlignment(Qt.AlignRight)

    @pyqtSlot(bool)
    def on_act_FontBold_triggered(self, checked):  # 粗体
        print(checked)
        if not self.selectionModel.hasSelection():
            return
        selectIndex = self.selectionModel.selectedIndexes()
        for index in selectIndex:
            item = self.itemModel.itemFromIndex(index)
            font = item.font()
            font.setBold(checked)
            item.setFont(font)

    @pyqtSlot()
    def on_act_ModelData_triggered(self):  # 模型数据更新显示
        self.ui.plainTextEdit.clear()
        lineStr = ''
        count = self.itemModel.columnCount()
        for i in range(count):  # 取表头数据
            if i == count - 1:
                item = self.itemModel.horizontalHeaderItem(count - 1)
                lineStr += item.text()
            else:
                item = self.itemModel.horizontalHeaderItem(i)
                lineStr += item.text() + '\t'
        self.ui.plainTextEdit.appendPlainText(lineStr)
        for i in range(self.itemModel.rowCount()):  # 取内容数据
            lineStr = ''
            for j in range(count):
                item = self.itemModel.item(i, j)
                if j == count - 1:
                    if item.checkState() == Qt.Checked:
                        lineStr += '1'
                    else:
                        lineStr += '0'
                else:
                    lineStr += item.text() + '\t'
            self.ui.plainTextEdit.appendPlainText(lineStr)

    @pyqtSlot()
    def on_act_SaveFile_triggered(self):  # 另存文件
        curPath = os.getcwd()
        filename, flt = QFileDialog.getSaveFileName(self, '保存文件', curPath, '井斜数据文件(*.txt);;所有文件(*.*)')
        if filename == '':
            return
        self.on_act_ModelData_triggered()
        with open(filename, 'w') as f:
            f.write(self.ui.plainTextEdit.toPlainText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyMainWindow()
    form.show()
    sys.exit(app.exec_())
