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
        MainWindow.resize(800, 460)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(self.groupBox)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_2.addWidget(self.plainTextEdit)
        self.verticalLayout_3.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.act_openFile = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/open.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_openFile.setIcon(icon)
        self.act_openFile.setObjectName("act_openFile")
        self.act_SaveFile = QtWidgets.QAction(MainWindow)
        self.act_SaveFile.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/save.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_SaveFile.setIcon(icon1)
        self.act_SaveFile.setObjectName("act_SaveFile")
        self.act_ModelData = QtWidgets.QAction(MainWindow)
        self.act_ModelData.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/images/export1.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_ModelData.setIcon(icon2)
        self.act_ModelData.setObjectName("act_ModelData")
        self.act_AddItem = QtWidgets.QAction(MainWindow)
        self.act_AddItem.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/images/append.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_AddItem.setIcon(icon3)
        self.act_AddItem.setObjectName("act_AddItem")
        self.act_InsterItem = QtWidgets.QAction(MainWindow)
        self.act_InsterItem.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/images/306.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_InsterItem.setIcon(icon4)
        self.act_InsterItem.setObjectName("act_InsterItem")
        self.act_DelItem = QtWidgets.QAction(MainWindow)
        self.act_DelItem.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/images/delete.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_DelItem.setIcon(icon5)
        self.act_DelItem.setObjectName("act_DelItem")
        self.act_Left = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/images/508.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_Left.setIcon(icon6)
        self.act_Left.setObjectName("act_Left")
        self.act_Center = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/images/510.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_Center.setIcon(icon7)
        self.act_Center.setObjectName("act_Center")
        self.act_Right = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/images/512.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_Right.setIcon(icon8)
        self.act_Right.setObjectName("act_Right")
        self.act_FontBold = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/images/500.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_FontBold.setIcon(icon9)
        self.act_FontBold.setCheckable(True)
        self.act_FontBold.setObjectName("act_FontBold")
        self.act_Exit = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/images/132.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_Exit.setIcon(icon10)
        self.act_Exit.setObjectName("act_Exit")
        self.mainToolBar.addAction(self.act_openFile)
        self.mainToolBar.addAction(self.act_SaveFile)
        self.mainToolBar.addAction(self.act_ModelData)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.act_AddItem)
        self.mainToolBar.addAction(self.act_InsterItem)
        self.mainToolBar.addAction(self.act_DelItem)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.act_Left)
        self.mainToolBar.addAction(self.act_Center)
        self.mainToolBar.addAction(self.act_Right)
        self.mainToolBar.addAction(self.act_FontBold)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.act_Exit)

        self.retranslateUi(MainWindow)
        self.act_Exit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Demo3_3,QTableView&QStandardItemModel"))
        self.groupBox.setTitle(_translate("MainWindow", "tableView"))
        self.groupBox_2.setTitle(_translate("MainWindow", "plainTextEdit"))
        self.mainToolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.act_openFile.setText(_translate("MainWindow", "打开文件"))
        self.act_SaveFile.setText(_translate("MainWindow", "另存文件"))
        self.act_ModelData.setText(_translate("MainWindow", "模型数据"))
        self.act_AddItem.setText(_translate("MainWindow", "添加行"))
        self.act_InsterItem.setText(_translate("MainWindow", "插入行"))
        self.act_DelItem.setText(_translate("MainWindow", "删除行"))
        self.act_Left.setText(_translate("MainWindow", "居左"))
        self.act_Center.setText(_translate("MainWindow", "居中"))
        self.act_Right.setText(_translate("MainWindow", "居右"))
        self.act_FontBold.setText(_translate("MainWindow", "粗体"))
        self.act_Exit.setText(_translate("MainWindow", "退出"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
