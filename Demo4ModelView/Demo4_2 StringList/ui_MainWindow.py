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
        MainWindow.resize(752, 453)
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
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_ResList = QtWidgets.QPushButton(self.groupBox)
        self.btn_ResList.setObjectName("btn_ResList")
        self.gridLayout.addWidget(self.btn_ResList, 0, 0, 1, 1)
        self.btn_insertItem = QtWidgets.QPushButton(self.groupBox)
        self.btn_insertItem.setObjectName("btn_insertItem")
        self.gridLayout.addWidget(self.btn_insertItem, 1, 1, 1, 1)
        self.btn_AddIns = QtWidgets.QPushButton(self.groupBox)
        self.btn_AddIns.setObjectName("btn_AddIns")
        self.gridLayout.addWidget(self.btn_AddIns, 1, 0, 1, 1)
        self.btn_DelCurrentItem = QtWidgets.QPushButton(self.groupBox)
        self.btn_DelCurrentItem.setObjectName("btn_DelCurrentItem")
        self.gridLayout.addWidget(self.btn_DelCurrentItem, 2, 0, 1, 1)
        self.btn_EmptyList = QtWidgets.QPushButton(self.groupBox)
        self.btn_EmptyList.setObjectName("btn_EmptyList")
        self.gridLayout.addWidget(self.btn_EmptyList, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.listView = QtWidgets.QListView(self.groupBox)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_ClearText = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_ClearText.setObjectName("btn_ClearText")
        self.verticalLayout_2.addWidget(self.btn_ClearText)
        self.btn_TextDisplay = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_TextDisplay.setObjectName("btn_TextDisplay")
        self.verticalLayout_2.addWidget(self.btn_TextDisplay)
        self.textEdit = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.verticalLayout_3.addWidget(self.splitter)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LabInfo = QtWidgets.QLabel(self.groupBox_3)
        self.LabInfo.setObjectName("LabInfo")
        self.horizontalLayout.addWidget(self.LabInfo)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Demo4_2 QListView的使用"))
        self.groupBox.setTitle(_translate("MainWindow", "QListView"))
        self.btn_ResList.setText(_translate("MainWindow", "恢复列表"))
        self.btn_insertItem.setText(_translate("MainWindow", "插入项"))
        self.btn_AddIns.setText(_translate("MainWindow", "添加项"))
        self.btn_DelCurrentItem.setText(_translate("MainWindow", "删除当前项"))
        self.btn_EmptyList.setText(_translate("MainWindow", "清空列表"))
        self.groupBox_2.setTitle(_translate("MainWindow", "QPlainTextEdit"))
        self.btn_ClearText.setText(_translate("MainWindow", "清空文本"))
        self.btn_TextDisplay.setText(_translate("MainWindow", "显示数据模型的StringList"))
        self.LabInfo.setText(_translate("MainWindow", "当前项的ModelIndex"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
