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
        MainWindow.resize(611, 402)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 611, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actTab_SetSize = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/230.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actTab_SetSize.setIcon(icon)
        self.actTab_SetSize.setObjectName("actTab_SetSize")
        self.actTab_SetHeader = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/516.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actTab_SetHeader.setIcon(icon1)
        self.actTab_SetHeader.setObjectName("actTab_SetHeader")
        self.actTab_Locate = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/images/304.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actTab_Locate.setIcon(icon2)
        self.actTab_Locate.setObjectName("actTab_Locate")
        self.act_Exit = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/images/132.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_Exit.setIcon(icon3)
        self.act_Exit.setObjectName("act_Exit")
        self.mainToolBar.addAction(self.actTab_SetSize)
        self.mainToolBar.addAction(self.actTab_SetHeader)
        self.mainToolBar.addAction(self.actTab_Locate)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.act_Exit)

        self.retranslateUi(MainWindow)
        self.act_Exit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Demo6_2 自定义对话框及其调用"))
        self.mainToolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actTab_SetSize.setText(_translate("MainWindow", "设置行数列数"))
        self.actTab_SetHeader.setText(_translate("MainWindow", "设置表头标题"))
        self.actTab_Locate.setText(_translate("MainWindow", "定位单元格"))
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
