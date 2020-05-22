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
        MainWindow.resize(800, 498)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(80, 40, 491, 301))
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.embedded_Widget = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/430.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.embedded_Widget.setIcon(icon)
        self.embedded_Widget.setObjectName("embedded_Widget")
        self.independent_Widget = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/806.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.independent_Widget.setIcon(icon1)
        self.independent_Widget.setObjectName("independent_Widget")
        self.embedded_MainWindow = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/images/808.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.embedded_MainWindow.setIcon(icon2)
        self.embedded_MainWindow.setObjectName("embedded_MainWindow")
        self.independent_MainWindow = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/images/804.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.independent_MainWindow.setIcon(icon3)
        self.independent_MainWindow.setObjectName("independent_MainWindow")
        self.act_Exit = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/images/132.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_Exit.setIcon(icon4)
        self.act_Exit.setObjectName("act_Exit")
        self.toolBar.addAction(self.embedded_Widget)
        self.toolBar.addAction(self.independent_Widget)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.embedded_MainWindow)
        self.toolBar.addAction(self.independent_MainWindow)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.act_Exit)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.act_Exit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Demo6_3 多窗口应用程序"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Page"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.embedded_Widget.setText(_translate("MainWindow", "嵌入式Widget"))
        self.independent_Widget.setText(_translate("MainWindow", "独立Widget窗口"))
        self.embedded_MainWindow.setText(_translate("MainWindow", "嵌入式MainWindow"))
        self.independent_MainWindow.setText(_translate("MainWindow", "独立MainWindow窗口"))
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
