# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QWDialogSize.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QWDialogSize(object):
    def setupUi(self, QWDialogSize):
        QWDialogSize.setObjectName("QWDialogSize")
        QWDialogSize.resize(419, 187)
        self.horizontalLayout = QtWidgets.QHBoxLayout(QWDialogSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(QWDialogSize)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.spin_ColCount = QtWidgets.QSpinBox(self.groupBox)
        self.spin_ColCount.setMinimum(1)
        self.spin_ColCount.setMaximum(500)
        self.spin_ColCount.setProperty("value", 6)
        self.spin_ColCount.setObjectName("spin_ColCount")
        self.gridLayout.addWidget(self.spin_ColCount, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.spin_RwoCount = QtWidgets.QSpinBox(self.groupBox)
        self.spin_RwoCount.setMinimum(1)
        self.spin_RwoCount.setMaximum(500)
        self.spin_RwoCount.setProperty("value", 10)
        self.spin_RwoCount.setObjectName("spin_RwoCount")
        self.gridLayout.addWidget(self.spin_RwoCount, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(QWDialogSize)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setContentsMargins(20, -1, 20, 9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnOK = QtWidgets.QPushButton(self.groupBox_2)
        self.btnOK.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/704.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOK.setIcon(icon)
        self.btnOK.setObjectName("btnOK")
        self.verticalLayout.addWidget(self.btnOK)
        self.btnCancel = QtWidgets.QPushButton(self.groupBox_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/706.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancel.setIcon(icon1)
        self.btnCancel.setObjectName("btnCancel")
        self.verticalLayout.addWidget(self.btnCancel)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(QWDialogSize)
        self.btnOK.clicked.connect(QWDialogSize.accept)
        self.btnCancel.clicked.connect(QWDialogSize.reject)
        QtCore.QMetaObject.connectSlotsByName(QWDialogSize)

    def retranslateUi(self, QWDialogSize):
        _translate = QtCore.QCoreApplication.translate
        QWDialogSize.setWindowTitle(_translate("QWDialogSize", "设置表格行数和列数"))
        self.groupBox.setTitle(_translate("QWDialogSize", "设置表格行数和列数"))
        self.label.setText(_translate("QWDialogSize", "列  数"))
        self.label_2.setText(_translate("QWDialogSize", "行  数"))
        self.btnOK.setText(_translate("QWDialogSize", "确定"))
        self.btnCancel.setText(_translate("QWDialogSize", "取消"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QWDialogSize = QtWidgets.QDialog()
    ui = Ui_QWDialogSize()
    ui.setupUi(QWDialogSize)
    QWDialogSize.show()
    sys.exit(app.exec_())
