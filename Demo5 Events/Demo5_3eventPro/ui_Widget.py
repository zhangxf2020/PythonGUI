# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(494, 320)
        self.LabelMove = QtWidgets.QLabel(Widget)
        self.LabelMove.setGeometry(QtCore.QRect(80, 40, 211, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.LabelMove.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.LabelMove.setFont(font)
        self.LabelMove.setObjectName("LabelMove")
        self.btnTest = QtWidgets.QPushButton(Widget)
        self.btnTest.setGeometry(QtCore.QRect(260, 110, 146, 51))
        self.btnTest.setObjectName("btnTest")
        self.btnMove = QtWidgets.QPushButton(Widget)
        self.btnMove.setGeometry(QtCore.QRect(40, 190, 141, 51))
        self.btnMove.setObjectName("btnMove")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Demo5_1,缺省的事件处理函数"))
        self.LabelMove.setText(_translate("Widget", "点击鼠标左键"))
        self.btnTest.setText(_translate("Widget", "Button at Center\n"
"resizeEvent事件"))
        self.btnMove.setText(_translate("Widget", "Movable Button\n"
"W,S,A,D键移动"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
