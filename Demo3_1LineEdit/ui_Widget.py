# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Widget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(352, 264)
        self.verticalLayout = QtWidgets.QVBoxLayout(Widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Widget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.editCount = QtWidgets.QLineEdit(self.groupBox)
        self.editCount.setObjectName("editCount")
        self.gridLayout.addWidget(self.editCount, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.editPrice = QtWidgets.QLineEdit(self.groupBox)
        self.editPrice.setObjectName("editPrice")
        self.gridLayout.addWidget(self.editPrice, 0, 3, 1, 1)
        self.btnCalculate = QtWidgets.QPushButton(self.groupBox)
        self.btnCalculate.setObjectName("btnCalculate")
        self.gridLayout.addWidget(self.btnCalculate, 1, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.editTotal = QtWidgets.QLineEdit(self.groupBox)
        self.editTotal.setObjectName("editTotal")
        self.gridLayout.addWidget(self.editTotal, 1, 3, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Widget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.spinPrice = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.spinPrice.setMaximum(1000.0)
        self.spinPrice.setProperty("value", 11.23)
        self.spinPrice.setObjectName("spinPrice")
        self.gridLayout_2.addWidget(self.spinPrice, 0, 3, 1, 1)
        self.spinTotal = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.spinTotal.setMaximum(10000.0)
        self.spinTotal.setObjectName("spinTotal")
        self.gridLayout_2.addWidget(self.spinTotal, 1, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 2, 1, 1)
        self.spinCount = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinCount.setMaximum(1000)
        self.spinCount.setProperty("value", 6)
        self.spinCount.setObjectName("spinCount")
        self.gridLayout_2.addWidget(self.spinCount, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.label.setBuddy(self.editCount)
        self.label_2.setBuddy(self.editPrice)
        self.label_3.setBuddy(self.editTotal)
        self.label_4.setBuddy(self.spinCount)
        self.label_5.setBuddy(self.spinPrice)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Form"))
        self.groupBox.setTitle(_translate("Widget", "QLineEdit输入和显示数值"))
        self.label.setText(_translate("Widget", "数 量(&N)"))
        self.editCount.setText(_translate("Widget", "16"))
        self.label_2.setText(_translate("Widget", "单 价(&P)"))
        self.editPrice.setText(_translate("Widget", "12.37"))
        self.btnCalculate.setText(_translate("Widget", "计算总价"))
        self.label_3.setText(_translate("Widget", "总 价(&T)"))
        self.groupBox_2.setTitle(_translate("Widget", "SpinBox输入和显示"))
        self.spinPrice.setPrefix(_translate("Widget", "$"))
        self.spinTotal.setPrefix(_translate("Widget", "$"))
        self.label_6.setText(_translate("Widget", "自动计算总价"))
        self.label_4.setText(_translate("Widget", "数 量"))
        self.label_5.setText(_translate("Widget", "单 价"))
        self.spinCount.setSuffix(_translate("Widget", " kg"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
