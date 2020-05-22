# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QWDialogHeaders.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QWDialogHeaders(object):
    def setupUi(self, QWDialogHeaders):
        QWDialogHeaders.setObjectName("QWDialogHeaders")
        QWDialogHeaders.resize(445, 436)
        self.horizontalLayout = QtWidgets.QHBoxLayout(QWDialogHeaders)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(QWDialogHeaders)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listView = QtWidgets.QListView(self.groupBox)
        self.listView.setObjectName("listView")
        self.verticalLayout_2.addWidget(self.listView)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btnOK = QtWidgets.QPushButton(QWDialogHeaders)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/704.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOK.setIcon(icon)
        self.btnOK.setObjectName("btnOK")
        self.verticalLayout.addWidget(self.btnOK)
        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem1)
        self.btnCancel = QtWidgets.QPushButton(QWDialogHeaders)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/706.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancel.setIcon(icon1)
        self.btnCancel.setObjectName("btnCancel")
        self.verticalLayout.addWidget(self.btnCancel)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(QWDialogHeaders)
        self.btnOK.clicked.connect(QWDialogHeaders.accept)
        self.btnCancel.clicked.connect(QWDialogHeaders.reject)
        QtCore.QMetaObject.connectSlotsByName(QWDialogHeaders)

    def retranslateUi(self, QWDialogHeaders):
        _translate = QtCore.QCoreApplication.translate
        QWDialogHeaders.setWindowTitle(_translate("QWDialogHeaders", "设置表头标题"))
        self.groupBox.setTitle(_translate("QWDialogHeaders", "表头标题"))
        self.btnOK.setText(_translate("QWDialogHeaders", "确定"))
        self.btnCancel.setText(_translate("QWDialogHeaders", "取消"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QWDialogHeaders = QtWidgets.QDialog()
    ui = Ui_QWDialogHeaders()
    ui.setupUi(QWDialogHeaders)
    QWDialogHeaders.show()
    sys.exit(app.exec_())
