# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QWDialoglocate.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QWDialogLocate(object):
    def setupUi(self, QWDialogLocate):
        QWDialogLocate.setObjectName("QWDialogLocate")
        QWDialogLocate.resize(421, 195)
        self.horizontalLayout = QtWidgets.QHBoxLayout(QWDialogLocate)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(QWDialogLocate)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.spinColumn = QtWidgets.QSpinBox(self.groupBox)
        self.spinColumn.setObjectName("spinColumn")
        self.gridLayout.addWidget(self.spinColumn, 0, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.spinRow = QtWidgets.QSpinBox(self.groupBox)
        self.spinRow.setObjectName("spinRow")
        self.gridLayout.addWidget(self.spinRow, 1, 1, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.editCellText = QtWidgets.QLineEdit(self.groupBox)
        self.editCellText.setObjectName("editCellText")
        self.gridLayout.addWidget(self.editCellText, 2, 1, 1, 2)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(QWDialogLocate)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnSetText = QtWidgets.QPushButton(self.groupBox_2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/322.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSetText.setIcon(icon)
        self.btnSetText.setObjectName("btnSetText")
        self.verticalLayout.addWidget(self.btnSetText)
        self.btnClose = QtWidgets.QPushButton(self.groupBox_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/132.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClose.setIcon(icon1)
        self.btnClose.setObjectName("btnClose")
        self.verticalLayout.addWidget(self.btnClose)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(QWDialogLocate)
        self.btnClose.clicked.connect(QWDialogLocate.close)
        QtCore.QMetaObject.connectSlotsByName(QWDialogLocate)

    def retranslateUi(self, QWDialogLocate):
        _translate = QtCore.QCoreApplication.translate
        QWDialogLocate.setWindowTitle(_translate("QWDialogLocate", "单元格定位与文字设置"))
        self.label.setText(_translate("QWDialogLocate", "列  号"))
        self.checkBox.setText(_translate("QWDialogLocate", "列增"))
        self.label_2.setText(_translate("QWDialogLocate", "行  号"))
        self.checkBox_2.setText(_translate("QWDialogLocate", "行增"))
        self.label_3.setText(_translate("QWDialogLocate", "设定文字"))
        self.btnSetText.setText(_translate("QWDialogLocate", "设定文字"))
        self.btnClose.setText(_translate("QWDialogLocate", "关  闭"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QWDialogLocate = QtWidgets.QDialog()
    ui = Ui_QWDialogLocate()
    ui.setupUi(QWDialogLocate)
    QWDialogLocate.show()
    sys.exit(app.exec_())
