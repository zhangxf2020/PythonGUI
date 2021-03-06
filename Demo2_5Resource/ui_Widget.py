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
        Widget.resize(400, 324)
        self.verticalLayout = QtWidgets.QVBoxLayout(Widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Widget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.sliderSetAge = QtWidgets.QSlider(self.groupBox)
        self.sliderSetAge.setMaximum(100)
        self.sliderSetAge.setProperty("value", 50)
        self.sliderSetAge.setOrientation(QtCore.Qt.Horizontal)
        self.sliderSetAge.setObjectName("sliderSetAge")
        self.gridLayout.addWidget(self.sliderSetAge, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.editAgeInt = QtWidgets.QLineEdit(self.groupBox)
        self.editAgeInt.setObjectName("editAgeInt")
        self.gridLayout.addWidget(self.editAgeInt, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.editAgeStr = QtWidgets.QLineEdit(self.groupBox)
        self.editAgeStr.setObjectName("editAgeStr")
        self.gridLayout.addWidget(self.editAgeStr, 2, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Widget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.editNameInput = QtWidgets.QLineEdit(self.groupBox_2)
        self.editNameInput.setObjectName("editNameInput")
        self.gridLayout_2.addWidget(self.editNameInput, 0, 1, 1, 1)
        self.btnSetName = QtWidgets.QPushButton(self.groupBox_2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/322.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSetName.setIcon(icon)
        self.btnSetName.setObjectName("btnSetName")
        self.gridLayout_2.addWidget(self.btnSetName, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.editNameHello = QtWidgets.QLineEdit(self.groupBox_2)
        self.editNameHello.setObjectName("editNameHello")
        self.gridLayout_2.addWidget(self.editNameHello, 1, 1, 1, 2)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.frame_Button = QtWidgets.QFrame(Widget)
        self.frame_Button.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_Button.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Button.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Button.setObjectName("frame_Button")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_Button)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btnClose = QtWidgets.QPushButton(self.frame_Button)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/132.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClose.setIcon(icon1)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout.addWidget(self.btnClose)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.frame_Button)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)
        Widget.setTabOrder(self.sliderSetAge, self.editAgeInt)
        Widget.setTabOrder(self.editAgeInt, self.editAgeStr)
        Widget.setTabOrder(self.editAgeStr, self.editNameInput)
        Widget.setTabOrder(self.editNameInput, self.btnSetName)
        Widget.setTabOrder(self.btnSetName, self.editNameHello)
        Widget.setTabOrder(self.editNameHello, self.btnClose)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Form"))
        self.groupBox.setTitle(_translate("Widget", "年龄设置"))
        self.label.setText(_translate("Widget", "设置年龄(0~100)"))
        self.label_2.setText(_translate("Widget", "ageChanged(int)响应"))
        self.label_3.setText(_translate("Widget", "ageChanged(str)响应"))
        self.groupBox_2.setTitle(_translate("Widget", "姓名设置"))
        self.label_4.setText(_translate("Widget", "输入姓名"))
        self.editNameInput.setText(_translate("Widget", "Mike"))
        self.btnSetName.setText(_translate("Widget", "设置姓名"))
        self.label_5.setText(_translate("Widget", "nameChanged(str)响应"))
        self.btnClose.setText(_translate("Widget", "关闭"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
