# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 521)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.groupBox = QtWidgets.QGroupBox(self.splitter_2)
        self.groupBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_InsertRow = QtWidgets.QPushButton(self.groupBox)
        self.btn_InsertRow.setObjectName("btn_InsertRow")
        self.gridLayout.addWidget(self.btn_InsertRow, 3, 0, 1, 1)
        self.chbox_TableCanEdited = QtWidgets.QCheckBox(self.groupBox)
        self.chbox_TableCanEdited.setChecked(True)
        self.chbox_TableCanEdited.setObjectName("chbox_TableCanEdited")
        self.gridLayout.addWidget(self.chbox_TableCanEdited, 7, 0, 1, 1)
        self.btn_ClearContents = QtWidgets.QPushButton(self.groupBox)
        self.btn_ClearContents.setObjectName("btn_ClearContents")
        self.gridLayout.addWidget(self.btn_ClearContents, 4, 1, 1, 1)
        self.btn_AutoRowWidth = QtWidgets.QPushButton(self.groupBox)
        self.btn_AutoRowWidth.setObjectName("btn_AutoRowWidth")
        self.gridLayout.addWidget(self.btn_AutoRowWidth, 5, 1, 1, 1)
        self.radiobtn_CellSelection = QtWidgets.QRadioButton(self.groupBox)
        self.radiobtn_CellSelection.setChecked(True)
        self.radiobtn_CellSelection.setObjectName("radiobtn_CellSelection")
        self.gridLayout.addWidget(self.radiobtn_CellSelection, 9, 1, 1, 1)
        self.btn_ReadIntoText = QtWidgets.QPushButton(self.groupBox)
        self.btn_ReadIntoText.setObjectName("btn_ReadIntoText")
        self.gridLayout.addWidget(self.btn_ReadIntoText, 6, 0, 1, 2)
        self.btn_AddRow = QtWidgets.QPushButton(self.groupBox)
        self.btn_AddRow.setObjectName("btn_AddRow")
        self.gridLayout.addWidget(self.btn_AddRow, 3, 1, 1, 1)
        self.btn_AutoRowHeight = QtWidgets.QPushButton(self.groupBox)
        self.btn_AutoRowHeight.setObjectName("btn_AutoRowHeight")
        self.gridLayout.addWidget(self.btn_AutoRowHeight, 5, 0, 1, 1)
        self.btn_DelCurrentRow = QtWidgets.QPushButton(self.groupBox)
        self.btn_DelCurrentRow.setObjectName("btn_DelCurrentRow")
        self.gridLayout.addWidget(self.btn_DelCurrentRow, 4, 0, 1, 1)
        self.radionbtn_RowSelection = QtWidgets.QRadioButton(self.groupBox)
        self.radionbtn_RowSelection.setObjectName("radionbtn_RowSelection")
        self.gridLayout.addWidget(self.radionbtn_RowSelection, 9, 0, 1, 1)
        self.btn_setRows = QtWidgets.QPushButton(self.groupBox)
        self.btn_setRows.setObjectName("btn_setRows")
        self.gridLayout.addWidget(self.btn_setRows, 1, 0, 1, 1)
        self.btn_IniTabularData = QtWidgets.QPushButton(self.groupBox)
        self.btn_IniTabularData.setObjectName("btn_IniTabularData")
        self.gridLayout.addWidget(self.btn_IniTabularData, 2, 0, 1, 2)
        self.chbox_RowBackground = QtWidgets.QCheckBox(self.groupBox)
        self.chbox_RowBackground.setChecked(True)
        self.chbox_RowBackground.setObjectName("chbox_RowBackground")
        self.gridLayout.addWidget(self.chbox_RowBackground, 7, 1, 1, 1)
        self.btn_setHeader = QtWidgets.QPushButton(self.groupBox)
        self.btn_setHeader.setAutoDefault(False)
        self.btn_setHeader.setDefault(False)
        self.btn_setHeader.setObjectName("btn_setHeader")
        self.gridLayout.addWidget(self.btn_setHeader, 0, 0, 1, 2)
        self.chbox_ShowRowHeader = QtWidgets.QCheckBox(self.groupBox)
        self.chbox_ShowRowHeader.setChecked(True)
        self.chbox_ShowRowHeader.setObjectName("chbox_ShowRowHeader")
        self.gridLayout.addWidget(self.chbox_ShowRowHeader, 8, 0, 1, 1)
        self.chbox_ShowListHeader = QtWidgets.QCheckBox(self.groupBox)
        self.chbox_ShowListHeader.setChecked(True)
        self.chbox_ShowListHeader.setObjectName("chbox_ShowListHeader")
        self.gridLayout.addWidget(self.chbox_ShowListHeader, 8, 1, 1, 1)
        self.spinBox_Row = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_Row.setProperty("value", 8)
        self.spinBox_Row.setObjectName("spinBox_Row")
        self.gridLayout.addWidget(self.spinBox_Row, 1, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.tableinfo = QtWidgets.QTableWidget(self.splitter)
        self.tableinfo.setRowCount(5)
        self.tableinfo.setColumnCount(4)
        self.tableinfo.setObjectName("tableinfo")
        item = QtWidgets.QTableWidgetItem()
        self.tableinfo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableinfo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableinfo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableinfo.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/boy.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        self.tableinfo.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableinfo.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableinfo.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableinfo.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableinfo.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableinfo.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableinfo.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/girl.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.tableinfo.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableinfo.setItem(3, 0, item)
        self.textEdit = QtWidgets.QPlainTextEdit(self.splitter)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.splitter_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Demo3_10 QTableWidget的使用"))
        self.btn_InsertRow.setText(_translate("MainWindow", "插入行"))
        self.chbox_TableCanEdited.setText(_translate("MainWindow", "表格可编辑"))
        self.btn_ClearContents.setText(_translate("MainWindow", "清空表格内容"))
        self.btn_AutoRowWidth.setText(_translate("MainWindow", "自动调节列宽"))
        self.radiobtn_CellSelection.setText(_translate("MainWindow", "单元格选择"))
        self.btn_ReadIntoText.setText(_translate("MainWindow", "读取表格内容到文本"))
        self.btn_AddRow.setText(_translate("MainWindow", "添加行"))
        self.btn_AutoRowHeight.setText(_translate("MainWindow", "自动调节行高"))
        self.btn_DelCurrentRow.setText(_translate("MainWindow", "删除当前行"))
        self.radionbtn_RowSelection.setText(_translate("MainWindow", "行选择"))
        self.btn_setRows.setText(_translate("MainWindow", "设置行数"))
        self.btn_IniTabularData.setText(_translate("MainWindow", "初始化表格数据"))
        self.chbox_RowBackground.setText(_translate("MainWindow", "间隔行底色"))
        self.btn_setHeader.setText(_translate("MainWindow", "设置表头"))
        self.chbox_ShowRowHeader.setText(_translate("MainWindow", "显示行表头"))
        self.chbox_ShowListHeader.setText(_translate("MainWindow", "显示列表头"))
        item = self.tableinfo.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "列1"))
        item = self.tableinfo.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "列2"))
        item = self.tableinfo.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "列3"))
        __sortingEnabled = self.tableinfo.isSortingEnabled()
        self.tableinfo.setSortingEnabled(False)
        item = self.tableinfo.item(0, 0)
        item.setText(_translate("MainWindow", "0行，0列"))
        item = self.tableinfo.item(0, 1)
        item.setText(_translate("MainWindow", "0行，1列"))
        item = self.tableinfo.item(0, 2)
        item.setText(_translate("MainWindow", "0行，2列"))
        item = self.tableinfo.item(0, 3)
        item.setText(_translate("MainWindow", "0行，3列"))
        item = self.tableinfo.item(1, 0)
        item.setText(_translate("MainWindow", "1行，0列"))
        item = self.tableinfo.item(1, 1)
        item.setText(_translate("MainWindow", "1行，1列"))
        item = self.tableinfo.item(1, 2)
        item.setText(_translate("MainWindow", "1行，2列"))
        item = self.tableinfo.item(2, 0)
        item.setText(_translate("MainWindow", "2行，0列"))
        item = self.tableinfo.item(2, 1)
        item.setText(_translate("MainWindow", "2行，1列"))
        item = self.tableinfo.item(3, 0)
        item.setText(_translate("MainWindow", "3行，0列"))
        self.tableinfo.setSortingEnabled(__sortingEnabled)
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
